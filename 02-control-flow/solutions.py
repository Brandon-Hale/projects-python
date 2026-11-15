"""
02 - Control flow: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def print_evens():
    for n in range(2, 21, 2):   # start at 2, stop before 21, step 2
        print(n)


def sum_to(n):
    total = 0
    for i in range(1, n + 1):   # + 1 because range excludes the stop value
        total += i
    return total


def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def fizzbuzz(n):
    if n % 15 == 0:             # check the most specific case first
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")


def first_multiple(start, stop, divisor):
    for n in range(start, stop):
        if n % divisor == 0:
            return n            # returning exits the loop too
    return None


def truthiness(value):
    return "truthy" if value else "falsy"


def day_type(day):
    match day:
        case "Saturday" | "Sunday":
            return "weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "weekday"
        case _:
            return "unknown"


def times_row(n):
    for i in range(1, 6):
        print(n * i, end=" ")
    print()


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
def ex01_print_evens():
    expected = "".join(f"{n}\n" for n in range(2, 21, 2))
    expect(output_of(print_evens), expected, "What print_evens() printed")


@check
def ex02_sum_to():
    expect(sum_to(4), 10, "sum_to(4)")
    expect(sum_to(100), 5050, "sum_to(100)")
    expect(sum_to(0), 0, "sum_to(0)")


@check
def ex03_grade():
    for score, letter in [(95, "A"), (90, "A"), (85, "B"), (72, "C"),
                          (60, "D"), (59, "F"), (0, "F"), (100, "A")]:
        expect(grade(score), letter, f"grade({score})")


@check
def ex04_fizzbuzz():
    for n, answer in [(15, "FizzBuzz"), (9, "Fizz"), (10, "Buzz"),
                      (7, "7"), (30, "FizzBuzz"), (1, "1")]:
        expect(fizzbuzz(n), answer, f"fizzbuzz({n})")


@check
def ex05_countdown():
    expect(output_of(countdown, 3), "3\n2\n1\nLiftoff!\n", "What countdown(3) printed")
    expect(output_of(countdown, 1), "1\nLiftoff!\n", "What countdown(1) printed")


@check
def ex06_first_multiple():
    expect(first_multiple(10, 20, 7), 14, "first_multiple(10, 20, 7)")
    expect(first_multiple(1, 5, 10), None, "first_multiple(1, 5, 10)")
    expect(first_multiple(3, 4, 3), 3, "first_multiple(3, 4, 3)")


@check
def ex07_truthiness():
    for value, answer in [(0, "falsy"), ("0", "truthy"), ([], "falsy"),
                          ([0], "truthy"), (None, "falsy"), ("", "falsy"),
                          (-1, "truthy"), ({}, "falsy")]:
        expect(truthiness(value), answer, f"truthiness({value!r})")


@check
def ex08_day_type():
    for day in ["Saturday", "Sunday"]:
        expect(day_type(day), "weekend", f"day_type({day!r})")
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        expect(day_type(day), "weekday", f"day_type({day!r})")
    expect(day_type("Caturday"), "unknown", 'day_type("Caturday")')


@check
def ex09_times_row():
    printed = output_of(times_row, 3)
    expect(printed.rstrip(), "3 6 9 12 15", "What times_row(3) printed")


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
