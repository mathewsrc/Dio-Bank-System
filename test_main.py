from click.testing import CliRunner
from main import is_valid_date, main, deposit, withdraw


def test_main():
    runner = CliRunner()
    result = runner.invoke(main, ["--version"])
    assert result.exit_code == 0


def test_valid_date_format():
    valid_dates = ["01-01-2022", "15-07-2023", "31-12-2024"]
    for date in valid_dates:
        assert is_valid_date(date)


def test_invalid_date_format():
    invalid_dates = ["2022-01-01", "15/07/2023", "31-12-24"]
    for date in invalid_dates:
        assert not is_valid_date(date)


def test_deposit_positive_value():
    balance = 100
    value = 50
    extract = ""

    new_balance, new_extract = deposit(balance, value, extract)
    assert new_balance == balance + value
    assert new_extract == f"Depósito: R$ {value:.2f}\n"


def test_deposit_negative_value():
    balance = 100
    value = -50
    extract = ""

    new_balance, new_extract = deposit(balance, value, extract)
    assert new_balance == balance
    assert new_extract == ""


def test_deposit_zero_value():
    balance = 100
    value = 0
    extract = ""

    new_balance, new_extract = deposit(balance, value, extract)
    assert new_balance == balance
    assert new_extract == ""


def test_withdraw_sufficient_balance():
    balance = 100
    value = 50
    extract = ""
    limit = 200
    number_withdrawals = 0
    withdrawal_limit = 3

    new_balance, new_extract = withdraw(
        balance=balance,
        value=value,
        extract=extract,
        limit=limit,
        number_withdrawals=number_withdrawals,
        withdrawal_limit=withdrawal_limit,
    )

    assert new_balance == balance - value
    assert new_extract == f"Saque: R$ {value:.2f}\n"


def test_withdraw_insufficient_balance():
    balance = 100
    value = 150
    extract = ""
    limit = 200
    number_withdrawals = 0
    withdrawal_limit = 3

    new_balance, new_extract = withdraw(
        balance=balance,
        value=value,
        extract=extract,
        limit=limit,
        number_withdrawals=number_withdrawals,
        withdrawal_limit=withdrawal_limit,
    )

    assert new_balance == balance
    assert new_extract == ""


def test_withdraw_exceeded_limit():
    balance = 100
    value = 250
    extract = ""
    limit = 200
    number_withdrawals = 0
    withdrawal_limit = 3

    new_balance, new_extract = withdraw(
        balance=balance,
        value=value,
        extract=extract,
        limit=limit,
        number_withdrawals=number_withdrawals,
        withdrawal_limit=withdrawal_limit,
    )

    assert new_balance == balance
    assert new_extract == ""


def test_withdraw_exceeded_withdrawal_limit():
    balance = 100
    value = 50
    extract = ""
    limit = 200
    number_withdrawals = 3
    withdrawal_limit = 3

    new_balance, new_extract = withdraw(
        balance=balance,
        value=value,
        extract=extract,
        limit=limit,
        number_withdrawals=number_withdrawals,
        withdrawal_limit=withdrawal_limit,
    )

    assert new_balance == balance
    assert new_extract == ""


def test_withdraw_zero_value():
    balance = 100
    value = 0
    extract = ""
    limit = 200
    number_withdrawals = 0
    withdrawal_limit = 3

    new_balance, new_extract = withdraw(
        balance=balance,
        value=value,
        extract=extract,
        limit=limit,
        number_withdrawals=number_withdrawals,
        withdrawal_limit=withdrawal_limit,
    )

    assert new_balance == balance
    assert new_extract == ""
