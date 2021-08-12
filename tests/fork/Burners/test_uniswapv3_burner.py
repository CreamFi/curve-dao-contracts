import pytest

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(UniswapV3Burner, alice, receiver):
    yield UniswapV3Burner.deploy(receiver, receiver, alice, alice, {"from": alice})


EURT = "0xC581b735A1688071A1746c968e0798D642EDE491"
TOKENS = [
    (EURT, "0x742d35cc6634c0532925a3b844bc454e4438f44e"),
]


@pytest.mark.parametrize("token,whale", TOKENS)
def test_burn(MintableTestToken, USDC, alice, receiver, burner, token, whale):
    token = MintableTestToken.from_abi("token", token, abi=ERC20)

    amount = 1000 * (10 ** token.decimals())
    token.transfer(alice, amount, {"from": whale})
    assert token.balanceOf(alice) == amount

    token.approve(burner, 2 ** 256 - 1, {"from": alice})
    burner.add_burnable_coin(token.address, 500)
    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert USDC.balanceOf(alice) == 0
    assert USDC.balanceOf(burner) == 0
    assert USDC.balanceOf(receiver) > 0
