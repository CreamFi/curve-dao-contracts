import pytest

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(UniswapLPBurner, alice, receiver):
    yield UniswapLPBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


UNISWAP_LP_DAI_ETH = "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11"
UNISWAP_LP_ETH_USDT = "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852"
UNISWAP_LP_USDC_ETH = "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc"
UNISWAP_LP_WBTC_ETH = "0xbb2b8038a1640196fbe3e38816f3e67cba72d940"
SUSHI_LP_DAI_ETH = "0xc3d03e4f041fd4cd388c549ee2a29a9e5075882f"
SUSHI_LP_ETH_USDT = "0x06da0fd433c1a5d7a4faa01111c044910a184553"
SUSHI_LP_SUSHI_ETH = "0x795065dcc9f64b5614c407a6efdc400da6221fb0"
SUSHI_LP_USDC_ETH = "0x397ff1542f962076d0bfe58ea045ffa2d347aca0"
SUSHI_LP_WBTC_ETH = "0xceff51756c56ceffca006cd410b03ffc46dd3a58"
SUSHI_LP_YFI_ETH = "0x088ee5007c98a9677165d78dd2109ae4a3d04d0c"

TOKENS = [
    UNISWAP_LP_DAI_ETH,
    UNISWAP_LP_ETH_USDT,
    UNISWAP_LP_USDC_ETH,
    UNISWAP_LP_WBTC_ETH,
    SUSHI_LP_DAI_ETH,
    SUSHI_LP_ETH_USDT,
    SUSHI_LP_SUSHI_ETH,
    SUSHI_LP_USDC_ETH,
    SUSHI_LP_WBTC_ETH,
    SUSHI_LP_YFI_ETH,
]


@pytest.mark.parametrize("token", TOKENS)
def test_burn(MintableTestToken, DAI, WETH, alice, receiver, burner, token):
    coin = MintableTestToken.from_abi("testToken", token, abi=ERC20)
    amount = 10 ** coin.decimals()
    mint_success = False
    fails = 0
    while not mint_success and fails < 5:
        try:
            coin._mint_for_testing(alice, amount, {"from": alice})
            mint_success = True
        except Exception:
            fails += 1
            amount /= 2
    coin.approve(burner, 2 ** 256 - 1, {"from": alice})

    burner.burn(coin, {"from": alice})

    assert coin.balanceOf(alice) == 0
    assert coin.balanceOf(burner) == 0
    assert coin.balanceOf(receiver) == 0

    assert WETH.balanceOf(alice) == 0
    assert WETH.balanceOf(burner) == 0
    assert WETH.balanceOf(receiver) > 0
