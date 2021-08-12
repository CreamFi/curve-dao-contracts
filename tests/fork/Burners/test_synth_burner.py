import pytest
from brownie import SynthBurner

from abi.ERC20 import ERC20


@pytest.fixture(scope="module")
def burner(alice, receiver):
    yield SynthBurner.deploy(receiver, receiver, alice, alice, {"from": alice})


SEUR = "0xD71eCFF9342A5Ced620049e616c5035F1dB98620"
SUSD = "0x57Ab1ec28D129707052df4dF418D58a2D46d5f51"
ZERO_ADDRESS = "0x" + "0" * 40


def test_burn(MintableTestToken, alice, receiver, burner, chain):
    seur = MintableTestToken.from_abi("seur", SEUR, abi=ERC20)
    susd = MintableTestToken.from_abi("susd", SUSD, abi=ERC20)
    whale = "0xCA55F9C4E77f7B8524178583b0f7c798De17fD54"

    amount = 10 ** seur.decimals()
    seur.transfer(alice, amount, {"from": whale})

    assert seur.balanceOf(alice) == amount
    assert seur.balanceOf(burner) == 0
    assert seur.balanceOf(receiver) == 0

    seur.approve(burner, 2 ** 256 - 1, {"from": alice})
    burner.add_synths([SEUR] + [ZERO_ADDRESS] * 9)
    burner.burn(seur, {"from": alice})

    assert seur.balanceOf(alice) == 0
    assert seur.balanceOf(burner) == 0
    assert seur.balanceOf(receiver) == 0

    # after an exchange, it takes 10 minute before the susd can be transferred out.
    assert susd.balanceOf(alice) == 0
    assert susd.balanceOf(burner) > 0
    assert susd.balanceOf(receiver) == 0

    chain.sleep(60 * 10)
    chain.mine()

    burner_susd_balance = susd.balanceOf(burner)
    burner.burn(seur, {"from": alice})

    assert susd.balanceOf(alice) == 0
    assert susd.balanceOf(burner) == 0
    assert susd.balanceOf(receiver) == burner_susd_balance
