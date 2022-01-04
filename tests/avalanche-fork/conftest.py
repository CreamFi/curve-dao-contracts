import pytest
from brownie_tokens import MintableForkToken

from abi.ERC20 import ERC20


class _MintableTestToken(MintableForkToken):
    def __init__(self, address):
        super().__init__(address)


@pytest.fixture(scope="session")
def MintableTestToken():
    yield _MintableTestToken


@pytest.fixture(scope="module")
def USDC():
    yield _MintableTestToken.from_abi(
        "USDC", "0xA7D7079b0FEaD91F3e65f86E8915Cb59c1a4C664", abi=ERC20
    )
