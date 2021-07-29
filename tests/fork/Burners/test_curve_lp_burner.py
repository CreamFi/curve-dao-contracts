import brownie
import pytest

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(CurveLPBurner, alice, receiver):
    yield CurveLPBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


CrvSETH = "0xa3d87fffce63b53e0d54faa1cc983b7eb0b74a9c"
CrvSTETH = "0x06325440d014e39736583c165c2963ba99faf14e"
DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
COINS = {
    CrvSETH: WETH,
    CrvSTETH: WETH,
}


@pytest.mark.parametrize("token,result_token", [(k, v) for k, v in COINS.items()])
def test_burn(MintableTestToken, alice, receiver, burner, token, result_token):
    token = MintableTestToken.from_abi("test", token, abi=ERC20)
    result_token = MintableTestToken.from_abi("test", result_token, abi=ERC20)
    amount = 10 ** token.decimals()

    token._mint_for_testing(alice, amount, {"from": alice})
    token.approve(burner, 2 ** 256 - 1, {"from": alice})

    assert token.balanceOf(alice) == amount
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0
    burner.add_swap_data(token)
    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert result_token.balanceOf(alice) == 0
    assert result_token.balanceOf(burner) == 0
    assert result_token.balanceOf(receiver) > 0


def test_burn_invalid_token(MintableTestToken, alice, burner, receiver):
    unapproved_token_address = (
        "0xBfedbcbe27171C418CDabC2477042554b1904857"  # yVault:Curve rETH Pool
    )
    unapproved_token = MintableTestToken.from_abi("yVCRVrETH", unapproved_token_address, abi=ERC20)
    amount = 10 ** unapproved_token.decimals()
    unapproved_token._mint_for_testing(alice, amount, {"from": alice})
    # revert when token is not added to burnable_tokens
    with brownie.reverts("token not burnable"):
        burner.burn(unapproved_token_address, {"from": alice})


def test_burn_old_token(MintableTestToken, alice, burner, receiver):
    token_address = "0xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8"  # yCRV
    pool = "0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3"
    result_token_address = "0x6b175474e89094c44da98b954eedeac495271d0f"  # DAI

    token = MintableTestToken.from_abi("test", token_address, abi=ERC20)
    result_token = MintableTestToken.from_abi("result_test", result_token_address, abi=ERC20)
    amount = 10 ** token.decimals()
    token._mint_for_testing(alice, amount, {"from": alice})
    assert token.balanceOf(alice) == amount
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    burner.add_old_swap_data(token_address, pool, result_token_address)
    token.approve(burner, 2 ** 256 - 1, {"from": alice})
    burner.burn(token_address, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert result_token.balanceOf(alice) == 0
    assert result_token.balanceOf(burner) == 0
    assert result_token.balanceOf(receiver) > 0
