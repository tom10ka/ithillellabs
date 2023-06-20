def test_account_init_balance(test_account_deposit):
    assert test_account_deposit.balance == 0


def test_account_withdraw(test_account_deposit):
    test_account_deposit.balance = 1000
    test_account_deposit.withdraw_money(500)
    assert test_account_deposit.balance == 500


def test_account_credit_allowed_deposit(test_account_deposit):
    assert test_account_deposit.credit_allowed is False


def test_account_change_credit_status_deposit(test_account_deposit):
    test_account_deposit.change_credit_status(True)
    assert test_account_deposit.credit_allowed is True


def test_account_deposit_money(test_account_deposit):
    test_account_deposit.balance = 1000
    test_account_deposit.deposit_money(600)
    assert test_account_deposit.balance == 1600
