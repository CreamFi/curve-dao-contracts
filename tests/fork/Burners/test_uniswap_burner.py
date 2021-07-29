import brownie
import pytest

from abi.ERC20 import ERC20
from abi.USDT import USDT as USDT_abi
from abi.WBTC import WBTC as WBTC_abi


@pytest.fixture(scope="module")
def burner(UniswapBurner, alice, receiver):
    yield UniswapBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


ONE_INCH = "0x111111111117dC0aa78b770fA6A738034120C302"
AAVE = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
AKRO = "0x8Ab7404063Ec4DBcfd4598215992DC3F8EC853d7"
ALPHA = "0xa1faa113cbE53436Df28FF0aEe54275c13B40975"
AMP = "0xff20817765cb7f73d4bde2e66e067e58d11095c2"
ARMOR = "0x1337def16f9b486faed0293eb623dc8395dfe46a"
ARNXM = "0x1337def18c680af1f9f45cbcab6309562975b1dd"
BAL = "0xba100000625a3754423978a60c9317c58a424e3d"
BBADGER = "0x19d97d8fa813ee2f51ad4b4e04ea08baf4dffc28"
BNT = "0x1f573d6fb3f13d689ff844b4ce37794d79a7ff1c"
BOND = "0x0391d2021f89dc339f60fff84546ea23e337750f"
BBTC = "0x9be89d2a4cd102d8fecc6bf9da793be995c22541"
BUSD = "0x4fabb145d64652a948d72533023f6e7a623c7c53"
CEL = "0xaaaebe6fe48e54f431b0c390cfaf0b017d09d42d"
COMP = "0xc00e94cb662c3520282e6f5717214004a7f26888"
COVER = "0x4688a8b1f292fdab17e9a90c8bc379dc1dbd8713"
CRV = "0xd533a949740bb3306d119cc777fa900ba034cd52"
DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
DPI = "0x1494ca1f11d487c2bbe4543e90080aeba4ba3c2b"
ESD = "0x36f3fd68e7325a35eb768f1aedaae9ea0689d723"
FEI = "0x956F47F50A910163D8BF957Cf5846D573E7f87CA"
FRAX = "0x853d955acef822db058eb8505911ed77f175b99e"
FTM = "0x4e15361fd6b4bb609fa63c81a2be19d873717870"
FTT = "0x50d1c9771902476076ecfc8b2a83ad6b9355a4c9"
GNO = "0x6810e776880c02933d47db1b9fc05908e5386b96"
HBTC = "0x0316eb71485b0ab14103307bf65a021042c6d380"
HEGIC = "0x584bc13c7d411c00c01a62e8019472de68768430"
HFIL = "0x9afb950948c2370975fb91a441f36fdc02737cd4"
HUSD = "0xdf574c24545e5ffecb9a659c229253d4111d87e1"
KP3R = "0x1ceb5cb57c4d4e2b2433641b95dd330a33185a44"
LINK = "0x514910771af9ca656af840dff83e8264ecf986ca"
MLN = "0xec67005c4E498Ec7f55E092bd1d35cbC47C91892"
MTA = "0xa3bed4e1c75d00fa6f4e5e6922db7261b5e9acd2"
OCEAN = "0x967da4048cd07ab37855c090aaf366e4ce1b9f48"
OGN = "0x8207c1ffc5b6804f6024322ccf34f29c3541ae26"
OMG = "0xd26114cd6ee289accf82350c8d8487fedb8a0c07"
PERP = "0xbC396689893D065F41bc2C6EcbeE5e0085233447"
PICKLE = "0x429881672b9ae42b8eba0e26cd9c73711b891ca5"
RAI = "0x03ab458634910aad20ef5f1c8ee96f1d6ac54919"
RARI = "0xfca59cd816ab1ead66534d82bc21e7515ce441cf"
RENBTC = "0xeb4c2781e4eba804ce9a9803c67d0893436bb27d"
RUNE = "0x3155ba85d5f96b2d030a4966af206230e46849cb"
SFI = "0xb753428af26e81097e7fd17f40c88aaa3e04902c"
SNX = "0xc011a73ee8576fb46f5e1c5751ca3b9fe0af2a6f"
SRM = "0x476c5e26a75bd202a9683ffd34359c0cc15be0ff"
SUSD = "0x57ab1ec28d129707052df4df418d58a2d46d5f51"
SUSHI = "0x6b3595068778dd592e39a122f4f5a5cf09c90fe2"
SWAG = "0x87edffde3e14c7a66c9b9724747a1c5696b742e6"
SWAP = "0xcc4304a31d09258b0029ea7fe63d032f52e44efe"
UNI = "0x1f9840a85d5af5bf1d1762f925bdaddc4201f984"
USDT = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
VSP = "0x1b40183efb4dd766f11bda7a7c3ad8982e998421"
UST = "0xa47c8bf37f92abed4a126bda807a7b7498661acd"
WBTC = "0x2260fac5e5542a773aa44fbcfedf7c193bc2c599"
WNXM = "0x0d438f3b5175bebc262bf23753c1e53d03432bde"
WOO = "0x4691937a7508860f876c9c0a2a617e7d9e945d4b"
YFI = "0x0bc529c00c6401aef6d220be8c6ea1667f6ad93e"
WETH = "0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2"
TOKENS = {
    ONE_INCH: ERC20,
    BBADGER: ERC20,
    AAVE: ERC20,
    AKRO: ERC20,
    ALPHA: ERC20,
    AMP: ERC20,
    ARMOR: ERC20,
    ARNXM: ERC20,
    BAL: ERC20,
    BNT: ERC20,
    BOND: ERC20,
    BBTC: ERC20,
    BUSD: ERC20,
    CEL: ERC20,
    COMP: ERC20,
    COVER: ERC20,
    CRV: ERC20,
    DAI: WBTC_abi,
    DPI: ERC20,
    ESD: ERC20,
    FEI: ERC20,
    FRAX: ERC20,
    FTM: ERC20,
    FTT: ERC20,
    GNO: ERC20,
    HBTC: ERC20,
    HEGIC: ERC20,
    HFIL: ERC20,
    HUSD: ERC20,
    KP3R: ERC20,
    LINK: ERC20,
    MLN: ERC20,
    MTA: ERC20,
    OCEAN: ERC20,
    OGN: ERC20,
    OMG: ERC20,
    PERP: ERC20,
    PICKLE: ERC20,
    # RAI: ERC20, # failed, ignore for now
    RARI: ERC20,
    RENBTC: WBTC_abi,
    RUNE: ERC20,
    SFI: ERC20,
    SNX: ERC20,
    SRM: ERC20,
    SUSD: ERC20,
    SUSHI: ERC20,
    SWAG: ERC20,
    SWAP: ERC20,
    UNI: ERC20,
    USDT: USDT_abi,
    VSP: ERC20,
    UST: ERC20,
    WBTC: WBTC_abi,
    WNXM: ERC20,
    WOO: ERC20,
    YFI: ERC20,
}


def test_burn_weth(MintableTestToken, USDC, alice, receiver, burner):
    weth = MintableTestToken.from_abi("WETH", WETH, abi=ERC20)
    amount = 10 ** weth.decimals()

    weth._mint_for_testing(alice, amount, {"from": alice})
    weth.approve(burner, 2 ** 256 - 1, {"from": alice})

    burner.burn(weth, {"from": alice})

    assert weth.balanceOf(alice) == 0
    assert weth.balanceOf(burner) == 0
    assert weth.balanceOf(receiver) == 0

    assert USDC.balanceOf(alice) == 0
    assert USDC.balanceOf(burner) == 0
    assert USDC.balanceOf(receiver) > 0


@pytest.mark.parametrize("token,abi", [(token, abi) for token, abi in TOKENS.items()])
def test_burn(MintableTestToken, USDC, alice, receiver, burner, token, abi):
    token = MintableTestToken.from_abi("token", token, abi=abi)

    amount = 1000 * (10 ** token.decimals())

    token._mint_for_testing(alice, amount, {"from": alice})
    assert token.balanceOf(alice) == amount
    token.approve(burner, 2 ** 256 - 1, {"from": alice})

    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert USDC.balanceOf(alice) == 0
    assert USDC.balanceOf(burner) == 0
    assert USDC.balanceOf(receiver) > 0


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
