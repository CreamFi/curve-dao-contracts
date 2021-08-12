import brownie
import pytest

from abi.ERC20 import ERC20


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


# Iron Bank
EURS = "0xdb25f211ab05b1c97d595516f45794528a807ad8"

TOKENS = [
    (ONE_INCH, "0x5e89f8d81c74e311458277ea1be3d3247c7cd7d1"),
    (BBADGER, "0xa9429271a28f8543efffa136994c0839e7d7bf77"),
    (AAVE, "0x4da27a545c0c5b758a6ba100e3a049001de870f5"),
    (AKRO, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (ALPHA, "0x580cE7B92F185D94511c9636869d28130702F68E"),
    (AMP, "0xec0527db0ba7c32d899fa100bc9ccadf40ca491c"),
    (ARMOR, "0x1f28ed9d4792a567dad779235c2b766ab84d8e33"),
    (ARNXM, "0x28a55c4b4f9615fde3cdaddf6cc01fcf2e38a6b0"),
    (BAL, "0xba12222222228d8ba445958a75a0704d566bf2c8"),
    (BNT, "0x4c9a2bd661d640da3634a4988a9bd2bc0f18e5a9"),
    (BOND, "0x4cae362d7f227e3d306f70ce4878e245563f3069"),
    (BBTC, "0xf977814e90da44bfa03b6295a0616a897441acec"),
    (BUSD, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (CEL, "0x84e1f49a6b65882c7365b6a775999cfcb481f22f"),
    (COMP, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (COVER, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (CRV, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (DAI, "0x5d3a536e4d6dbd6114cc1ead35777bab948e3643"),
    (DPI, "0x2A537Fa9FFaea8C1A41D3C2B68a9cb791529366D"),
    (ESD, "0xD5d5A7CB1807364CDE0BAd51D0a7D758943aB114"),
    (FRAX, "0xd632f22692fac7611d2aa1c0d552930d43caed3b"),
    (FTM, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (FTT, "0xd769010d3813bafaf4addbfe258eafd07828bb83"),
    (GNO, "0xec83f750adfe0e52a8b0dba6eeb6be5ba0bee535"),
    (HBTC, "0xa929022c9107643515f5c777ce9a910f0d1e490c"),
    (HEGIC, "0x736f85bf359e3e2db736d395ed8a4277123eeee1"),
    (HFIL, "0xa929022c9107643515f5c777ce9a910f0d1e490c"),
    (HUSD, "0xa929022c9107643515f5c777ce9a910f0d1e490c"),
    (KP3R, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (LINK, "0xF977814e90dA44bFA03b6295A0616a897441aceC"),
    (MLN, "0xd8f8a53945bcfbbc19da162aa405e662ef71c40d"),
    (MTA, "0x3dd46846eed8d147841ae162c8425c08bd8e1b41"),
    (OCEAN, "0xd5e6219a79c5cc61b9074331d1b05a6f35c5a48a"),
    (OGN, "0xf977814e90da44bfa03b6295a0616a897441acec"),
    (OMG, "0xf977814e90da44bfa03b6295a0616a897441acec"),
    (PERP, "0xc49f76a596d6200e4f08f8931d15b69dd1f8033e"),
    (PICKLE, "0xbbcf169ee191a1ba7371f30a1c344bfc498b29cf"),
    (RARI, "0xfdff6b56cce39482032b27140252ff4f16432785"),
    (RENBTC, "0x4f868c1aa37fcf307ab38d215382e88fca6275e2"),
    (RUNE, "0x46e3a8c8135647b48b2e82198e42e0c69eacbab8"),
    (SFI, "0x90b397f0962c3bc624f8ebc810c1e68655a4d0d3"),
    (SNX, "0x767ecb395def19ab8d1b2fcc89b3ddfbed28fd6b"),
    (SRM, "0x0548f59fee79f8832c299e01dca5c76f034f558e"),
    (SUSD, "0xa5f7a39e55d7878bc5bd754ee5d6bd7a7662355b"),
    (SUSHI, "0xcbe6b83e77cdc011cc18f6f0df8444e5783ed982"),
    (SWAG, "0x9c1be2d263024b07afb9d7f9bccb06775aba94b0"),
    (SWAP, "0x5a753021ce28cbc5a7c51f732ba83873d673d8cc"),
    (UNI, "0xe3953d9d317b834592ab58ab2c7a6ad22b54075d"),
    (USDT, "0xa929022c9107643515f5c777ce9a910f0d1e490c"),
    (VSP, "0x9520b477aa81180e6ddc006fc09fb6d3eb4e807a"),
    (UST, "0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf"),
    (WBTC, "0xccf4429db6322d5c611ee964527d42e5d685dd6a"),
    (WNXM, "0xf977814e90da44bfa03b6295a0616a897441acec"),
    (WOO, "0xf0b8660476ea1af0f363de8816e3e7cd1c8f1fde"),
    (YFI, "0x3ff33d9162ad47660083d7dc4bc02fb231c81677"),
    (EURS, "0x0ce6a5ff5217e38315f87032cf90686c96627caa"),
    (FEI, "0xf5bce5077908a1b7370b9ae04adc565ebd643966"),
    (RAI, "0x86b0e9e05f0295adb39799a402d2992d10439454"),
]


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


@pytest.mark.parametrize("token,whale", TOKENS)
def test_burn(MintableTestToken, USDC, alice, receiver, burner, token, whale):
    token = MintableTestToken.from_abi("token", token, abi=ERC20)
    amount = 1000 * (10 ** token.decimals())
    token.transfer(alice, amount, {"from": whale})

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
