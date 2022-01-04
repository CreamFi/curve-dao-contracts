# import brownie
import pytest

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(TraderJoeBurner, alice, receiver):
    yield TraderJoeBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


WAVAX = "0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7"
USDT = "0xc7198437980c041c805A1EDcbA50c1Ce5db95118"
WETH = "0x49D5c2BdFfac6CE2BFdB6640F4F80f226bc10bAB"
DAI = "0xd586E7F844cEa2F87f50152665BCbc2C279D8d70"
WBTC = "0x50b7545627a5162F82A992c33b87aDc75187B218"
USDC_OLD = "0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e"
LINK = "0x5947BB275c521040051D82396192181b413227A3"

TOKENS = [
    (WAVAX, "0xdfe521292ece2a4f44242efbcd66bc594ca9714b"),
    (USDT, "0x532e6537fea298397212f09a61e03311686f548e"),
    (WETH, "0x53f7c5869a859f0aec3d334ee8b4cf01e3492f21"),
    (DAI, "0x47afa96cdc9fab46904a55a6ad4bf6660b53c38a"),
    (WBTC, "0x686bef2417b6dc32c50a3cbfbcc3bb60e1e9a15d"),
    (USDC_OLD, "0xbf14db80d9275fb721383a77c00ae180fc40ae98"),
    (LINK, "0x2842a5d74a0374a4749784477c686d27f82a9e03"),
]


@pytest.mark.parametrize("token,whale", TOKENS)
def test_burn(MintableTestToken, USDC, alice, receiver, burner, token, whale):
    token = MintableTestToken.from_abi("token", token, abi=ERC20)
    amount = 1000 * (10 ** token.decimals())
    token.transfer(alice, amount, {"from": whale})

    token.approve(burner, 2 ** 256 - 1, {"from": alice})

    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert USDC.balanceOf(alice) == 0
    assert USDC.balanceOf(burner) == 0
    assert USDC.balanceOf(receiver) > 0


"""
def test_burn_unburnable(MintableTestToken, USDC, alice, burner):
    # CMC Rank 500 coin, not available in either sushi or uniswap
    turtle = MintableTestToken.from_abi(
        "turtle", "0xf3afdc2525568ffe743801c8c54bdea1704c9adb", abi=ERC20
    )

    amount = 10 ** turtle.decimals()

    turtle._mint_for_testing(alice, amount, {"from": alice})
    turtle.approve(burner, 2 ** 256 - 1, {"from": alice})
    with brownie.reverts("neither Uniswap nor Sushiswap has liquidity pool for this token"):
        burner.burn(turtle, {"from": alice})
"""
