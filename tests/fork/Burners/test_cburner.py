import pytest
from brownie import CBurner

from abi.ERC20 import ERC20

CDAI = "0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643"
CUSDT = "0xf650C3d88D12dB855b8bf7D11Be6C55A4e07dCC9"

DAI = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
USDT = "0xdac17f958d2ee523a2206206994597c13d831ec7"


TOKENS = {
    CDAI: DAI,
    CUSDT: USDT,
}


@pytest.mark.parametrize(
    "token,result_token", [(token, result_token) for token, result_token in TOKENS.items()]
)
def test_burn(MintableTestToken, alice, receiver, bob, token, result_token):
    burner = CBurner.deploy(receiver, receiver, alice, alice, bob, {"from": alice})
    token = MintableTestToken.from_abi("test", token, abi=ERC20)
    result_token = MintableTestToken.from_abi("result_test", result_token, abi=ERC20)
    amount = 10 ** token.decimals()

    token._mint_for_testing(alice, amount, {"from": alice})
    token.approve(burner, 2 ** 256 - 1, {"from": alice})

    assert token.balanceOf(alice) == amount
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert result_token.balanceOf(alice) == 0
    assert result_token.balanceOf(burner) == 0
    assert result_token.balanceOf(receiver) > 0


def test_burn_cusdc(MintableTestToken, alice, receiver, bob):
    CUSDC = "0x39AA39c021dfbaE8faC545936693aC917d5E7563"
    USDC = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    burner = CBurner.deploy(receiver, receiver, alice, alice, bob, {"from": alice})
    token = MintableTestToken.from_abi("test", CUSDC, abi=ERC20)
    result_token = MintableTestToken.from_abi("test", USDC, abi=ERC20)
    amount = 10 ** token.decimals()

    token._mint_for_testing(alice, amount, {"from": alice})
    token.approve(burner, 2 ** 256 - 1, {"from": alice})

    assert token.balanceOf(alice) == amount
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    burner.burn(token, {"from": alice})

    assert token.balanceOf(alice) == 0
    assert token.balanceOf(burner) == 0
    assert token.balanceOf(receiver) == 0

    assert result_token.balanceOf(alice) == 0
    assert result_token.balanceOf(burner) == 0
    assert result_token.balanceOf(receiver) == 0
    assert result_token.balanceOf(bob) > 0
