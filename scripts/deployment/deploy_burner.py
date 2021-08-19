from brownie import (
    CBurner,
    CurveLPBurner,
    FeeDistributor,
    MUSDBurner,
    SynthBurner,
    UniswapBurner,
    UniswapLPBurner,
    UniswapV3Burner,
    USDCBurner,
    VvspBurner,
    XSushiBurner,
    YearnVaultBurner,
    accounts,
)

VOTING_ESCROW = "0x3986425b96F11972d31C78ff340908832C5c0043"
OWNER_ADMIN = "0x6D5a7597896A703Fe8c85775B23395a48f971305"
EMERGENCY_ADMIN = "0x197939c1ca20C2b506d6811d8B6CDB3394471074"
RECOVERY = "0x6D5a7597896A703Fe8c85775B23395a48f971305"

"""
Example for running this script on mainnet-fork
> $ export WEB3_INFURA_PROJECT_ID="INFURA_PROJECT_ID"
> $ brownie run scripts/deployment/deploy_burner.py development --network mainnet-fork
"""


def development():
    deployer = accounts[0]

    yv_ib = "0x27b7b1ad7288079A66d12350c828D3C00A6F07d7"

    start_time = 1627344000  # July 27, 2021 12:00:00 AM GMT+0
    distributor = FeeDistributor.deploy(
        VOTING_ESCROW, start_time, yv_ib, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )
    distributor.toggle_allow_checkpoint_token({"from": OWNER_ADMIN})

    # deploy and setup usdc burner
    usdc_burner = USDCBurner.deploy(
        distributor, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )

    # deploy and setup uniswap burner
    uniswap_burner = UniswapBurner.deploy(
        usdc_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )

    # deploy and setup uniswap lp burner
    UniswapLPBurner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )

    # deploy and setup vvsp burner
    VvspBurner.deploy(uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer})

    # deploy and setup xsushi burner
    XSushiBurner.deploy(uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer})

    # deploy and setup musd burner
    MUSDBurner.deploy(usdc_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer})

    # deploy and setup synth burner
    synth_burner = SynthBurner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )
    SEUR = "0xD71eCFF9342A5Ced620049e616c5035F1dB98620"
    ZERO_ADDRESS = "0x" + "0" * 40
    synth_burner.add_synths([SEUR] + [ZERO_ADDRESS] * 9, {"from": OWNER_ADMIN})

    # deploy and setup compound burner
    CBurner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, usdc_burner, {"from": deployer}
    )

    # deploy and setup uniswap v3 burner
    uniswapv3_burner = UniswapV3Burner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )
    EURT = "0xC581b735A1688071A1746c968e0798D642EDE491"
    uniswapv3_burner.add_burnable_coin(EURT, 500, {"from": OWNER_ADMIN})

    # deploy and setup curve lp burner
    curve_lp_burner = CurveLPBurner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )

    # setup curveLP token with old interface
    yCRV_address = "0xdf5e0e81dff6faf3a7e52ba697820c5e32d806a8"
    yCRV_pool = "0xbbc81d23ea2c3ec7e56d39296f0cbb648873a5d3"
    Crv3_address = "0x6c3F90f043a72FA612cbac8115EE7e52BDe6E490"
    Crv3_pool = "0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7"
    DAI = "0x6b175474e89094c44da98b954eedeac495271d0f"
    curve_lp_burner.add_old_swap_data(yCRV_address, yCRV_pool, DAI, {"from": OWNER_ADMIN})
    curve_lp_burner.add_old_swap_data(Crv3_address, Crv3_pool, DAI, {"from": OWNER_ADMIN})

    # setup curveLP token with new interface
    CrvSETH = "0xa3d87fffce63b53e0d54faa1cc983b7eb0b74a9c"
    CrvSTETH = "0x06325440d014e39736583c165c2963ba99faf14e"
    curve_lp_burner.add_swap_data(CrvSETH, {"from": OWNER_ADMIN})
    curve_lp_burner.add_swap_data(CrvSTETH, {"from": OWNER_ADMIN})

    # deploy and setup yearn vault burner that sends result to uniswap burner
    yearn_vault_burner = YearnVaultBurner.deploy(
        uniswap_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )
    yWeth = "0xe1237aa7f535b0cc33fd973d66cbf830354d16c7"
    yvWeth = "0xa9fe4601811213c340e850ea305481aff02f5b28"
    yearn_vault_burner.add_burnable_coin(yWeth, {"from": OWNER_ADMIN})
    yearn_vault_burner.add_burnable_coin(yvWeth, {"from": OWNER_ADMIN})

    # deploy and setup another yearn vault burner that sends result to curve lp burner
    yearn_vault_burner_2 = YearnVaultBurner.deploy(
        curve_lp_burner, RECOVERY, OWNER_ADMIN, EMERGENCY_ADMIN, {"from": deployer}
    )
    # Yearn Vault Curve: sETH -> withdraw and get Curve.fi ETH/sETH LP token
    yVaultsEth = "0x986B4AFF588A109C09B50A03F42E4110E29D353F"
    # Yearn Vault Curve: stETH -> withdraw and get Curve.fi ETH/stETH LP token
    yVaultstEth = "0xDCD90C7F6324CFA40D7169EF80B12031770B4325"
    # Yearn Vault Curve: yUSD(yDAI/yUSDC/yUSDT/yTUSD) -> withdraw and get Curve.fi yCRV token
    yUSD = "0x4B5BFD52124784745C1071DCB244C6688D2533D3"
    # Yearn Vault 3CRV -> withdraw and get 3CRV
    Y3Crvc = "0x9cA85572E6A3EbF24dEDd195623F188735A5179f"
    yearn_vault_burner_2.add_burnable_coin(yVaultsEth, {"from": OWNER_ADMIN})
    yearn_vault_burner_2.add_burnable_coin(yVaultstEth, {"from": OWNER_ADMIN})
    yearn_vault_burner_2.add_burnable_coin(yUSD, {"from": OWNER_ADMIN})
    yearn_vault_burner_2.add_burnable_coin(Y3Crvc, {"from": OWNER_ADMIN})

    print("Deployment complete")
