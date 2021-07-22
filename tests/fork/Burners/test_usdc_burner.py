import pytest
from brownie import UniswapBurner

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(USDCBurner, alice, receiver):
    yield USDCBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
YVAULT_IB3_CRV = "0x27b7b1ad7288079A66d12350c828D3C00A6F07d7"


def test_burn_weth(MintableTestToken, alice, receiver, burner):
    # deploy uniswap burner to burn weth
    uniswap_burner = UniswapBurner.deploy(burner.address, alice, alice, alice, {"from": alice})

    # setup weth and send to alice
    weth = MintableTestToken.from_abi("WETH", WETH, abi=ERC20)
    amount = 10 ** weth.decimals()
    weth._mint_for_testing(alice, amount, {"from": alice})
    weth.approve(uniswap_burner, 2 ** 256 - 1, {"from": alice})

    # burn weth
    uniswap_burner.burn(weth, {"from": alice})
    # burned weth and sent usdc to usdc burner
    usdc = MintableTestToken.from_abi("USDC", USDC, abi=ERC20)
    assert usdc.balanceOf(alice) == 0
    assert usdc.balanceOf(uniswap_burner) == 0
    assert usdc.balanceOf(burner) > 0

    # burn usdc
    burner.burn(usdc, {"from": alice})

    yvault_ib3_crv = MintableTestToken.from_abi("YVAULT_IB3_CRV", YVAULT_IB3_CRV, abi=ERC20)
    assert yvault_ib3_crv.balanceOf(alice) == 0
    assert yvault_ib3_crv.balanceOf(burner) == 0
    assert yvault_ib3_crv.balanceOf(receiver) > 0
