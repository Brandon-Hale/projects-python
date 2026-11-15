"""
Example pytest tests for calculator.py

Run (from this folder, after `pip install pytest`):
    pytest -v
"""
import pytest

from calculator import BankAccount, add, average, divide, is_leap_year


# --- Plain test functions ---------------------------------------------------------
def test_add_two_positives():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, 3) == 1


def test_divide():
    assert divide(10, 4) == 2.5


def test_average_float_result():
    assert average([0.1, 0.2]) == pytest.approx(0.15)   # floats: use approx


# --- Expecting exceptions ----------------------------------------------------------
def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_average_empty_list_raises():
    with pytest.raises(ValueError, match="empty"):
        average([])


# --- Parametrised: one test function, many cases --------------------------------------
@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),    # divisible by 4
        (2023, False),   # not divisible by 4
        (1900, False),   # divisible by 100 but not 400
        (2000, True),    # divisible by 400
    ],
)
def test_is_leap_year(year, expected):
    assert is_leap_year(year) == expected


# --- Fixtures: shared setup -------------------------------------------------------------
@pytest.fixture
def account():
    return BankAccount(balance=100)


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70


def test_overdraw_raises_and_keeps_balance(account):
    with pytest.raises(ValueError):
        account.withdraw(500)
    assert account.balance == 100


@pytest.mark.parametrize("bad_amount", [0, -10])
def test_deposit_must_be_positive(account, bad_amount):
    with pytest.raises(ValueError):
        account.deposit(bad_amount)


# --- Built-in fixtures --------------------------------------------------------------------
def test_tmp_path_gives_a_fresh_folder(tmp_path):
    file = tmp_path / "hello.txt"
    file.write_text("hi", encoding="utf-8")
    assert file.read_text(encoding="utf-8") == "hi"


def test_capsys_captures_print(capsys):
    print("hello from the test")
    captured = capsys.readouterr()
    assert captured.out == "hello from the test\n"
