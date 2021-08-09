import brownie
import pytest
from brownie import MUSDBurner

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(alice, receiver):
    yield MUSDBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


MUSD = "0xe2f2a5C287993345a840Db3B0845fbC70f5935a5"


def test_burn(MintableTestToken, alice, receiver, USDC, burner):
    musd = MintableTestToken.from_abi("musd", MUSD, abi=ERC20)
    amount = 10 ** musd.decimals()

    musd._mint_for_testing(alice, amount, {"from": alice})
    musd.approve(burner, 2 ** 256 - 1, {"from": alice})

    assert musd.balanceOf(alice) == amount
    assert musd.balanceOf(burner) == 0
    assert musd.balanceOf(receiver) == 0

    burner.burn(musd, {"from": alice})

    assert musd.balanceOf(alice) == 0
    assert musd.balanceOf(burner) == 0
    assert musd.balanceOf(receiver) == 0

    assert USDC.balanceOf(alice) == 0
    assert USDC.balanceOf(burner) == 0
    assert USDC.balanceOf(receiver) > 0


def test_burn_invalid_token(MintableTestToken, alice, USDC, burner):
    usdc = MintableTestToken.from_abi("usdc", USDC.address, abi=ERC20)
    with brownie.reverts("only allows burning musd"):
        burner.burn(usdc, {"from": alice})
