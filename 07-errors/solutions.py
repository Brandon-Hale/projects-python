"""
07 - Errors: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default


def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return None


def validate_age(age):
    if not 0 <= age <= 150:
        raise ValueError(f"age must be between 0 and 150, got {age}")
    return age


class InsufficientFundsError(Exception):
    """Raised when trying to withdraw more than the balance."""


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"can't withdraw {amount} from {balance}")
    return balance - amount


def run_logged(func, log):
    log.append("start")
    try:
        return func()
    finally:
        log.append("done")   # runs even while `return` or an exception is in flight


def first_valid_number(texts):
    for text in texts:
        try:
            return int(text)
        except ValueError:
            continue   # `pass` would work here too - the loop moves on either way
    return None


def get_setting(config, key):
    try:
        return config[key]
    except KeyError as error:
        raise LookupError(f"missing setting: {key}") from error


# =============================================================================
# CHECKS - run this file with:  python solutions.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
from contextlib import redirect_stdout

_checks = []


def check(test):
    _checks.append(test)
    return test


def output_of(func, *args):
    """Run func and return everything it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args)
    return buffer.getvalue()


def expect(actual, expected, label):
    assert actual == expected, f"{label} should be {expected!r}, got {actual!r}"


def expect_raises(error_type, func, *args):
    """Check that func(*args) raises error_type. Returns the exception."""
    try:
        func(*args)
    except NotImplementedError:
        raise
    except error_type as error:
        return error
    raise AssertionError(f"{func.__name__}{args} should raise {error_type.__name__}")


@check
def ex01_safe_divide():
    expect(safe_divide(10, 2), 5.0, "safe_divide(10, 2)")
    expect(safe_divide(1, 0), None, "safe_divide(1, 0)")


@check
def ex02_parse_int():
    expect(parse_int("42"), 42, 'parse_int("42")')
    expect(parse_int("abc"), 0, 'parse_int("abc")')
    expect(parse_int("abc", -1), -1, 'parse_int("abc", -1)')


@check
def ex03_safe_get():
    expect(safe_get([1, 2, 3], 1), 2, "safe_get([1, 2, 3], 1)")
    expect(safe_get([1, 2, 3], 10), None, "safe_get([1, 2, 3], 10)")


@check
def ex04_validate_age():
    expect(validate_age(30), 30, "validate_age(30)")
    expect(validate_age(0), 0, "validate_age(0)")
    expect(validate_age(150), 150, "validate_age(150)")
    expect_raises(ValueError, validate_age, -1)
    expect_raises(ValueError, validate_age, 200)


@check
def ex05_withdraw():
    expect(withdraw(100, 30), 70, "withdraw(100, 30)")
    expect(withdraw(100, 100), 0, "withdraw(100, 100)")
    expect_raises(InsufficientFundsError, withdraw, 100, 300)


@check
def ex06_run_logged():
    log = []
    expect(run_logged(lambda: 42, log), 42, "run_logged(lambda: 42, log)")
    expect(log, ["start", "done"], "log after a successful call")

    def explode():
        raise RuntimeError("boom")

    log = []
    try:
        run_logged(explode, log)
    except RuntimeError:
        pass
    else:
        raise AssertionError("the RuntimeError from func should not be swallowed")
    expect(log, ["start", "done"], "log after func raised")


@check
def ex07_first_valid_number():
    expect(first_valid_number(["x", "", "12", "7"]), 12, 'first_valid_number(["x", "", "12", "7"])')
    expect(first_valid_number(["a", "b"]), None, 'first_valid_number(["a", "b"])')
    expect(first_valid_number([]), None, "first_valid_number([])")


@check
def ex08_get_setting():
    expect(get_setting({"port": 80}, "port"), 80, 'get_setting({"port": 80}, "port")')
    error = expect_raises(LookupError, get_setting, {}, "port")
    assert not isinstance(error, KeyError), "raise a plain LookupError, not the original KeyError"
    expect(str(error), "missing setting: port", "the error message")
    assert isinstance(error.__cause__, KeyError), "chain it with `raise ... from error`"


if __name__ == "__main__":
    passed = 0
    for test in _checks:
        try:
            test()
        except NotImplementedError:
            print(f"[TODO]  {test.__name__}")
        except AssertionError as error:
            print(f"[FAIL]  {test.__name__}: {error}")
        except Exception as error:
            print(f"[ERROR] {test.__name__}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"[PASS]  {test.__name__}")
    print(f"\n{passed}/{len(_checks)} exercises passing")
