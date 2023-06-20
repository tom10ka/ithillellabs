import pytest
# from faker import Faker
#
from models import Account, AccountType
#
# fake_gen = Faker(locale='uk_UA')


# @pytest.fixture(scope='session')  # default = function, class, module, session
# def new_client():
#     client = Client(
#         name=fake_gen.name(),
#         address=fake_gen.address()
#     )
#     yield client
#     del client


@pytest.fixture()
def test_account_deposit():
    account = Account(AccountType.DEPOSIT)
    return account


@pytest.fixture()
def test_account_current():
    account = Account(AccountType.CURRENT)
    return account
