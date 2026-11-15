"""
03 - Functions: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def power(base, exponent=2):
    return base ** exponent


def make_greeting(name, *, greeting="Hello"):
    return f"{greeting}, {name}!"


def total(*numbers):
    return sum(numbers)


def describe(**info):
    parts = []
    for key, value in info.items():
        parts.append(f"{key}={value}")
    return ", ".join(parts)


def divide(a, b):
    return a // b, a % b


def apply_twice(func, value):
    return func(func(value))


def make_multiplier(n):
    def multiply(x):
        return x * n      # `n` is remembered from the outer call
    return multiply
    # or simply:  return lambda x: x * n


def add_tag(tag, items=None):
    if items is None:
        items = []
    items.append(tag)
    return items


square = lambda x: x ** 2


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


def raises(error_type, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
    except error_type:
        return True
    return False


@check
def ex01_power():
    expect(power(2, 5), 32, "power(2, 5)")
    expect(power(3), 9, "power(3)")


@check
def ex02_make_greeting():
    expect(make_greeting("Ada", greeting="Hi"), "Hi, Ada!", 'make_greeting("Ada", greeting="Hi")')
    expect(make_greeting("Ada"), "Hello, Ada!", 'make_greeting("Ada")')
    assert raises(TypeError, make_greeting, "Ada", "Hi"), \
        "greeting should be keyword-only: make_greeting('Ada', 'Hi') should raise TypeError"


@check
def ex03_total():
    expect(total(1, 2, 3), 6, "total(1, 2, 3)")
    expect(total(), 0, "total()")
    expect(total(5), 5, "total(5)")


@check
def ex04_describe():
    expect(describe(name="Ada", age=36), "name=Ada, age=36", 'describe(name="Ada", age=36)')
    expect(describe(), "", "describe()")


@check
def ex05_divide():
    expect(divide(17, 5), (3, 2), "divide(17, 5)")
    expect(divide(10, 2), (5, 0), "divide(10, 2)")


@check
def ex06_apply_twice():
    expect(apply_twice(lambda x: x + 3, 10), 16, "apply_twice(lambda x: x + 3, 10)")
    expect(apply_twice(str.upper, "hi"), "HI", 'apply_twice(str.upper, "hi")')


@check
def ex07_make_multiplier():
    triple = make_multiplier(3)
    assert callable(triple), "make_multiplier(3) should return a function"
    expect(triple(5), 15, "make_multiplier(3)(5)")
    expect(make_multiplier(10)(7), 70, "make_multiplier(10)(7)")


@check
def ex08_add_tag():
    expect(add_tag("a"), ["a"], 'first add_tag("a")')
    expect(add_tag("b"), ["b"], 'then add_tag("b")')
    expect(add_tag("c", ["x"]), ["x", "c"], 'add_tag("c", ["x"])')


@check
def ex09_square():
    if square is None:
        raise NotImplementedError
    assert square.__name__ == "<lambda>", "square should be a lambda, not a def"
    expect(square(4), 16, "square(4)")


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
