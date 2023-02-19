"""
Test max fee functionality.
"""

import pytest

from .account import declare, invoke

from .shared import (
    CONTRACT_PATH,
    PREDEPLOY_ACCOUNT_CLI_ARGS,
    PREDEPLOYED_ACCOUNT_ADDRESS,
    PREDEPLOYED_ACCOUNT_PRIVATE_KEY
)
from .util import (
    assert_class_by_hash,
    assert_tx_status,
    deploy,
    devnet_in_background,
    ReturnCodeAssertionError,
)

        

@devnet_in_background(*PREDEPLOY_ACCOUNT_CLI_ARGS)
def test_invoke_with_max_fee_0():
    initial_balance, amount1, amount2 = 100, 13, 56
    deploy_info = deploy(CONTRACT_PATH, [str(initial_balance)])
    account_address = PREDEPLOYED_ACCOUNT_ADDRESS
    private_key = PREDEPLOYED_ACCOUNT_PRIVATE_KEY
    calls = [(deploy_info["address"], "increase_balance", [10, 20])]
    with pytest.raises(ReturnCodeAssertionError):
        invoke_tx_hash = invoke(calls, account_address, private_key, max_fee=0)

@devnet_in_background(*PREDEPLOY_ACCOUNT_CLI_ARGS, "--allow-max-fee-zero")
def test_invoke_with_max_fee_0_and_allow_max_fee_zero():
    initial_balance, amount1, amount2 = 100, 13, 56
    deploy_info = deploy(CONTRACT_PATH, [str(initial_balance)])
    account_address = PREDEPLOYED_ACCOUNT_ADDRESS
    private_key = PREDEPLOYED_ACCOUNT_PRIVATE_KEY
    calls = [(deploy_info["address"], "increase_balance", [10, 20])]
    invoke_tx_hash = invoke(calls, account_address, private_key, max_fee=0)
    assert_tx_status(invoke_tx_hash, "ACCEPTED_ON_L2")

@devnet_in_background()
def test_declare_with_max_fee_0():
    with pytest.raises(ReturnCodeAssertionError):
        declare_info = declare(
        contract_path=CONTRACT_PATH,
        account_address=PREDEPLOYED_ACCOUNT_ADDRESS,
        private_key=PREDEPLOYED_ACCOUNT_PRIVATE_KEY,
        max_fee=0,
    )

@devnet_in_background(*PREDEPLOY_ACCOUNT_CLI_ARGS, "--allow-max-fee-zero")
def test_declare_with_max_fee_0_and_allow_max_fee_zero():
    declare_info = declare(
        contract_path=CONTRACT_PATH,
        account_address=PREDEPLOYED_ACCOUNT_ADDRESS,
        private_key=PREDEPLOYED_ACCOUNT_PRIVATE_KEY,
        max_fee=0,
    )
    class_hash = declare_info["class_hash"]
    assert_class_by_hash(class_hash, CONTRACT_PATH)
