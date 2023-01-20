from brownie import FundMe, config, network, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVS


def deploy_fundme():

    # pass price feed address to fundme contract
    account = get_account()

    # if using goerli use address
    # otherwise deploy mocks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        priceFeedAddress = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        priceFeedAddress = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(
        priceFeedAddress,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    return fundme


def main():
    deploy_fundme()
