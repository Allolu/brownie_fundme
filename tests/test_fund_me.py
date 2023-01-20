from brownie import network, accounts, exceptions
import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVS
from scripts.deploy import deploy_fundme


def test_fund_withdraw():
    account = get_account()
    fundme = deploy_fundme()
    entrance_fee = fundme.getEntranceFee()
    tx = fundme.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fundme.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fundme.withdraw({"from": account})
    tx2.wait(1)
    assert fundme.addressToAmountFunded(account.address) == 0


def test_owner_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        pytest.skip("only for local testing")
    account = get_account()
    fundme = deploy_fundme()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundme.withdraw({"from": bad_actor})
