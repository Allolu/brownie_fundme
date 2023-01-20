from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVS = ["development", "ganache-local"]
FORKED_LOCAL_ENVS = ["mainnet-fork  "]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVS
        or network.show_active in FORKED_LOCAL_ENVS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(8, 2000 * 10**8, {"from": get_account()})
    print("Mocks Deployed! ")
