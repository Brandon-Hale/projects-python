"""
01 - Basics: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def greeting(name):
    return f"Hello, {name}!"


def average(a, b, c):
    return (a + b + c) / 3  # / always gives a float


def minutes_to_hours(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours}h {minutes}m"


def is_even(n):
    return n % 2 == 0  # the comparison already IS a bool, no if needed


def add_text_numbers(a, b):
    return int(a) + int(b)


def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def swap(a, b):
    return b, a


def type_name(value):
    return type(value).__name__


def print_name_card(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


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


@check
def ex01_greeting():
    expect(greeting("Ada"), "Hello, Ada!", 'greeting("Ada")')
    expect(greeting("Guido"), "Hello, Guido!", 'greeting("Guido")')


@check
def ex02_average():
    expect(average(1, 2, 3), 2.0, "average(1, 2, 3)")
    expect(average(1, 2, 4), 7 / 3, "average(1, 2, 4)")


@check
def ex03_minutes_to_hours():
    expect(minutes_to_hours(125), "2h 5m", "minutes_to_hours(125)")
    expect(minutes_to_hours(45), "0h 45m", "minutes_to_hours(45)")
    expect(minutes_to_hours(60), "1h 0m", "minutes_to_hours(60)")


@check
def ex04_is_even():
    expect(is_even(4), True, "is_even(4)")
    expect(is_even(7), False, "is_even(7)")
    expect(is_even(0), True, "is_even(0)")


@check
def ex05_add_text_numbers():
    expect(add_text_numbers("40", "2"), 42, 'add_text_numbers("40", "2")')
    expect(add_text_numbers("-5", "10"), 5, 'add_text_numbers("-5", "10")')


@check
def ex06_celsius_to_fahrenheit():
    expect(celsius_to_fahrenheit(100), 212.0, "celsius_to_fahrenheit(100)")
    expect(celsius_to_fahrenheit(0), 32.0, "celsius_to_fahrenheit(0)")
    expect(celsius_to_fahrenheit(-40), -40.0, "celsius_to_fahrenheit(-40)")


@check
def ex07_swap():
    expect(swap(1, 2), (2, 1), "swap(1, 2)")
    expect(swap("a", "b"), ("b", "a"), 'swap("a", "b")')


@check
def ex08_type_name():
    expect(type_name(3), "int", "type_name(3)")
    expect(type_name("hi"), "str", 'type_name("hi")')
    expect(type_name(2.5), "float", "type_name(2.5)")
    expect(type_name(None), "NoneType", "type_name(None)")


@check
def ex09_print_name_card():
    expect(output_of(print_name_card, "Ada", 36), "Name: Ada\nAge: 36\n",
           'What print_name_card("Ada", 36) printed')


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
