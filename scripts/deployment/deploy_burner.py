import time

from brownie import (
  FeeDistributor,
  USDCBurner,
  UniswapBurner,
  UniswapLPBurner,
  VvspBurner,
  XSushiBurner,
  CurveLPBurner,
  YearnVaultBurner,
  accounts,
  Contract
)

VOTING_ESCROW = "0x3986425b96F11972d31C78ff340908832C5c0043"
OWNER_ADMIN = "0x6D5a7597896A703Fe8c85775B23395a48f971305"
EMERGENCY_ADMIN = "0x197939c1ca20C2b506d6811d8B6CDB3394471074"
RECOVERY = "0x6D5a7597896A703Fe8c85775B23395a48f971305"

"""
Example for running this script on mainnet-fork
> $ WEB3_INFURA_PROJECT_ID="INFURA_PROJECT_ID" brownie run scripts/deployment/deploy_burner.py development --network mainnet-fork
"""

def development():
  deployer = accounts[0]

  yv_ib = Contract("0x27b7b1ad7288079A66d12350c828D3C00A6F07d7")

  start_time = int(time.time())
  distributor = FeeDistributor.deploy(
    VOTING_ESCROW,
    start_time,
    yv_ib,
    OWNER_ADMIN,
    EMERGENCY_ADMIN,
    {"from": deployer}
  )

  usdc_burner = USDCBurner.deploy(
    distributor, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  uniswap_burner = UniswapBurner.deploy(
    usdc_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  uniswap_lp_burner = UniswapLPBurner.deploy(
    uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  vvsp_burner = VvspBurner.deploy(
    uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  xsush_burner = XSushiBurner.deploy(
    uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  curve_lp_burner = CurveLPBurner.deploy(
    uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  yearn_vault_burner = YearnVaultBurner.deploy(
    uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  yearn_vault_burner_2 = YearnVaultBurner.deploy(
    curve_lp_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
  )

  print("Deployment complete")
