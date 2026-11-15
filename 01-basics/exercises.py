"""
01 - Basics: exercises

For each exercise:
  1. Read the description.
  2. Delete the `raise NotImplementedError` line.
  3. Write your code.
  4. Run this file:  python exercises.py

Stuck? Peek at solutions.py, but try first!
"""


# ---------------------------------------------------------------------------
# Exercise 1: Greeting
# Return the string "Hello, <name>!" using an f-string.
#   greeting("Ada")  ->  "Hello, Ada!"
# ---------------------------------------------------------------------------
def greeting(name):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: Average
# Return the average of three numbers. The result should be a float.
#   average(1, 2, 3)  ->  2.0
# ---------------------------------------------------------------------------
def average(a, b, c):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: Minutes to hours
# Given a total number of minutes, return a string like "2h 5m".
# Hint: use // and %
#   minutes_to_hours(125)  ->  "2h 5m"
#   minutes_to_hours(45)   ->  "0h 45m"
# ---------------------------------------------------------------------------
def minutes_to_hours(total_minutes):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: Is even?
# Return True if n is even, otherwise False. One line is enough!
#   is_even(4)  ->  True
#   is_even(7)  ->  False
# ---------------------------------------------------------------------------
def is_even(n):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: Add numbers stored as text
# Both arguments are strings containing whole numbers. Return their sum
# as an int.
#   add_text_numbers("40", "2")  ->  42
# ---------------------------------------------------------------------------
def add_text_numbers(a, b):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: Celsius to Fahrenheit
# F = C * 9 / 5 + 32
#   celsius_to_fahrenheit(100)  ->  212.0
# ---------------------------------------------------------------------------
def celsius_to_fahrenheit(celsius):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Swap
# Return the two values in the opposite order, separated by a comma.
# (This returns a "tuple", which you'll meet properly in module 04.)
#   swap(1, 2)  ->  (2, 1)
# ---------------------------------------------------------------------------
def swap(a, b):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: Type name
# Return the NAME of the value's type as a string.
# Hint: type(value) gives you the type, and every type has a __name__.
#   type_name(3)      ->  "int"
#   type_name("hi")   ->  "str"
#   type_name(None)   ->  "NoneType"
# ---------------------------------------------------------------------------
def type_name(value):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 9: Name card (printing)
# PRINT (don't return) two lines:
#   Name: <name>
#   Age: <age>
#   print_name_card("Ada", 36) prints:
#     Name: Ada
#     Age: 36
# ---------------------------------------------------------------------------
def print_name_card(name, age):
    raise NotImplementedError  # delete this line and write your code


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
