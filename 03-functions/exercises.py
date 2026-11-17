"""
03 - Functions: exercises

Delete each `raise NotImplementedError` line, write your code,
then run:  python exercises.py

Some exercises ask you to change the function SIGNATURE (the `def` line) too.
Those will show [ERROR] with a TypeError until you fix the `def` line - read
the error message, it tells you exactly what's wrong with the signature.
"""


# ---------------------------------------------------------------------------
# Exercise 1: Default parameter
# Return base raised to exponent. The exponent should default to 2.
# You need to change the `def` line to add the default value.
#   power(3)     ->  9
#   power(2, 5)  ->  32
# ---------------------------------------------------------------------------
def power(base, exponent=2):
    val = pow(base, exponent)
    return val


# ---------------------------------------------------------------------------
# Exercise 2: Keyword-only argument
# Return "<greeting>, <name>!". `greeting` must be KEYWORD-ONLY and
# default to "Hello". Change the `def` line (hint: a bare *).
#   make_greeting("Ada")                  ->  "Hello, Ada!"
#   make_greeting("Ada", greeting="Hi")   ->  "Hi, Ada!"
#   make_greeting("Ada", "Hi")            ->  TypeError (that's what we want!)
# ---------------------------------------------------------------------------
def make_greeting(name, *, greeting="Hello"):
    return f"{greeting}, {name}!"


# ---------------------------------------------------------------------------
# Exercise 3: Any number of arguments
# Accept ANY number of numbers and return their total.
# Change the `def` line to use *args.
#   total(1, 2, 3)  ->  6
#   total()         ->  0
# ---------------------------------------------------------------------------
def total(*numbers):
    return sum(numbers)


# ---------------------------------------------------------------------------
# Exercise 4: Keyword arguments to text
# Accept any keyword arguments and return them as "key=value" pairs joined
# by ", " in the order they were given. Change the `def` line to use **kwargs.
#   describe(name="Ada", age=36)  ->  "name=Ada, age=36"
#   describe()                    ->  ""
# Hint: build a list of strings, then ", ".join(the_list)
# ---------------------------------------------------------------------------
def describe(info):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: Return two things
# Return BOTH the quotient and remainder of a divided by b (in that order).
#   divide(17, 5)  ->  (3, 2)
# ---------------------------------------------------------------------------
def divide(a, b):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: Apply twice
# `func` is a function. Call it on `value`, then call it AGAIN on the result.
#   apply_twice(lambda x: x + 3, 10)  ->  16
# ---------------------------------------------------------------------------
def apply_twice(func, value):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Function factory (closure)
# Return a NEW FUNCTION that multiplies its argument by n.
#   triple = make_multiplier(3)
#   triple(5)  ->  15
# ---------------------------------------------------------------------------
def make_multiplier(n):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: Fix the mutable default bug
# This function has the classic shared-list bug. Fix it so that each call
# without `items` gets a brand new list.
#   add_tag("a")  ->  ["a"]
#   add_tag("b")  ->  ["b"]       (NOT ["a", "b"])
#   add_tag("c", ["x"])  ->  ["x", "c"]
# ---------------------------------------------------------------------------
def add_tag(tag, items=[]):
    raise NotImplementedError  # delete this line, fix the `def` line, and write your code
    items.append(tag)
    return items


# ---------------------------------------------------------------------------
# Exercise 9: Lambda
# Assign a LAMBDA (not a def) to `square` that returns its argument squared.
#   square(4)  ->  16
# ---------------------------------------------------------------------------
square = None  # replace None with a lambda


# =============================================================================
# CHECKS - run this file with:  python exercises.py
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
