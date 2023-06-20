def test_account_init_balance(test_account_current):
    assert test_account_current.balance == 0


def test_account_withdraw(test_account_current):
    test_account_current.balance = 1000
    test_account_current.withdraw_money(500)
    assert test_account_current.balance == 500


def test_account_credit_allowed_current(test_account_current):
    assert test_account_current.credit_allowed is True


def test_account_change_credit_status_current(test_account_current):
    test_account_current.change_credit_status(False)
    assert test_account_current.credit_allowed is False


def test_account_deposit_money(test_account_current):
    test_account_current.balance = 1000
    test_account_current.deposit_money(600)
    assert test_account_current.balance == 1600
