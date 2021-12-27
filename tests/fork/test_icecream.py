import pytest
from brownie import Contract, FeeDistributor, UniswapBurner, USDCBurner, VotingEscrow

from abi.ERC20 import ERC20

H = 3600
DAY = 86400
WEEK = 7 * DAY
MAXTIME = 126144000  # 4 years
TOL = 120 / WEEK


VOTING_ESCROW = "0x3986425b96F11972d31C78ff340908832C5c0043"
FEE_DISTRIBUTOR = "0x0Ca0f068edad122f09a39f99E7E89E705d6f6Ace"
CREAM = "0x2ba592f78db6436527729929aaf6c908497cb200"
YVAULT_IB3_CRV = "0x27b7b1ad7288079A66d12350c828D3C00A6F07d7"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
USDC_BURNER = "0x0980f2F0D2af35eF2c4521b2342D59db575303F7"
UNISWAP_BURNER = "0x79EA17bEE0a8dcb900737E8CAa247c8358A5dfa1"
WHALE = "0xd6d16B110ea9173d7cEB6CFe8Ca4060749A75f5c"


@pytest.mark.parametrize("day", range(1, 7))
def test_claim(web3, chain, accounts, MintableTestToken, day):
    yvault_ib3_crv = MintableTestToken.from_abi("YVAULT_IB3_CRV", YVAULT_IB3_CRV, abi=ERC20)
    whale = accounts.at(WHALE, True)
    fee_distributor = Contract.from_abi("FeeDistributor", FEE_DISTRIBUTOR, FeeDistributor.abi)

    # send money to fee distro, current mainnet fork block is 13059466
    # time Aug-20-2021 02:26:54 AM UTC+0
    yvault_ib3_crv.transfer(fee_distributor, 2831000, {"from": whale})

    # sleep for days
    chain.sleep(60 * 60 * 24 * day)
    chain.mine()
    # this user create_lock on Monday, Aug-16-2021 10:49:44 AM UTC+0
    # this user is entitled to fees burned between
    # Aug-19-2021 00:00:00 AM UTC + 0 to Aug-26-2021 00:00:00 AM UTC+0 (exclusive)
    user = accounts.at("0xcc876be657b5d3d80cb9d483fb846766a8b80185", True)
    initial_balance = yvault_ib3_crv.balanceOf(user)
    fee_distributor.claim(user, {"from": user})
    after_balance = yvault_ib3_crv.balanceOf(user)
    if day >= 6:
        assert after_balance > initial_balance
    else:
        assert after_balance == initial_balance


def test_claiming_ib3crv(alice, MintableTestToken, web3, chain, bob):
    # dao contracts
    fee_distributor = Contract.from_abi("FeeDistributor", FEE_DISTRIBUTOR, FeeDistributor.abi)
    voting_escrow = Contract("VotingEscrow", VOTING_ESCROW, VotingEscrow.abi)
    usdc_burner = Contract("USDCBurner", USDC_BURNER, USDCBurner.abi)
    uniswap_burner = Contract("UniswapBurner", UNISWAP_BURNER, UniswapBurner.abi)

    # tokens
    cream = MintableTestToken.from_abi("CREAM", CREAM, abi=ERC20)
    yvault_ib3_crv = MintableTestToken.from_abi("YVAULT_IB3_CRV", YVAULT_IB3_CRV, abi=ERC20)
    usdc = MintableTestToken.from_abi("USDC", USDC, abi=ERC20)
    weth = MintableTestToken.from_abi("WETH", WETH, abi=ERC20)

    # alice will be iceCream holder, bob will call burner.burn
    amount = 100 * 1e18
    cream._mint_for_testing(alice, amount, {"from": alice})
    weth._mint_for_testing(bob, amount, {"from": bob})

    assert voting_escrow.totalSupply() == 0
    assert voting_escrow.balanceOf(alice) == 0

    # Move to timing which is good for testing - beginning of a UTC week
    chain.sleep((chain[-1].timestamp // WEEK + 1) * WEEK - chain[-1].timestamp)
    chain.mine()

    # lock cream for iceCream
    cream.approve(voting_escrow.address, amount, {"from": alice})
    voting_escrow.create_lock(amount, chain[-1].timestamp + 8 * WEEK, {"from": alice})
    assert cream.balanceOf(alice) == 0
    assert voting_escrow.balanceOf(alice) > 0
    chain.sleep(WEEK)
    chain.mine()
    # burn fees for yvIB3CRV
    weth.approve(uniswap_burner, amount, {"from": bob})
    uniswap_burner.burn(WETH, {"from": bob})

    assert weth.balanceOf(bob) == 0
    assert usdc.balanceOf(usdc_burner) > 0

    usdc_burner.burn(USDC, {"from": bob})
    assert usdc.balanceOf(usdc_burner) == 0
    assert usdc.balanceOf(fee_distributor) == 0
    assert yvault_ib3_crv.balanceOf(fee_distributor) > 0

    # Sleep and Checkpoint
    for i in range(7):
        chain.sleep(WEEK)
        chain.mine()
        fee_distributor.checkpoint_token({"from": alice})
    fee_distributor.claim({"from": alice})
    assert yvault_ib3_crv.balanceOf(alice) > 0
