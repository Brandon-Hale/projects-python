"""
02 - Control flow: exercises

Delete each `raise NotImplementedError` line, write your code,
then run:  python exercises.py
"""


# ---------------------------------------------------------------------------
# Exercise 1: Print the evens
# Write a loop that PRINTS every even number from 2 to 20 (inclusive),
# one per line.
#   2
#   4
#   ...
#   20
# ---------------------------------------------------------------------------
def print_evens():
    for i in range(1, 21): # 0 index remember (20 inclusive)
        if i % 2 == 0:
            print(f"{i}")


# ---------------------------------------------------------------------------
# Exercise 2: Sum to n
# Use a loop to add up every whole number from 1 to n (inclusive) and
# return the total. (Don't use sum() - practise the loop!)
#   sum_to(4)  ->  10      (1 + 2 + 3 + 4)
# ---------------------------------------------------------------------------
def sum_to(n):
    total = 0;
    for i in range(n):
        total += i + 1
    return total


# ---------------------------------------------------------------------------
# Exercise 3: Grade
# Return a letter grade for a score from 0-100 using if/elif/else:
#   90+ -> "A",  80-89 -> "B",  70-79 -> "C",  60-69 -> "D",  below 60 -> "F"
# ---------------------------------------------------------------------------
def grade(score):
    grade = None
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade


# ---------------------------------------------------------------------------
# Exercise 4: FizzBuzz (single number)
# Return:
#   "FizzBuzz" if n is divisible by 3 AND 5
#   "Fizz"     if n is divisible by 3
#   "Buzz"     if n is divisible by 5
#   otherwise the number as a string, e.g. "7"
# ---------------------------------------------------------------------------
def fizzbuzz(n):
    fizz = n % 3 == 0
    buzz = n % 5 == 0

    if fizz and buzz:
        return "FizzBuzz"
    elif fizz:
        return "Fizz"
    elif buzz:
        return "Buzz"

    return f"{n}"

# ---------------------------------------------------------------------------
# Exercise 5: Countdown
# Use a WHILE loop to PRINT n down to 1, then print "Liftoff!"
#   countdown(3) prints:
#     3
#     2
#     1
#     Liftoff!
# ---------------------------------------------------------------------------
def countdown(n):
    while (n > 0):
        print(n)
        n = n - 1

    print("Liftoff!")

# ---------------------------------------------------------------------------
# Exercise 6: First multiple
# Loop through the numbers from `start` up to (but not including) `stop`.
# Return the first one divisible by `divisor`. Use `break` or an early `return`.
# If none is found, return None.
#   first_multiple(10, 20, 7)  ->  14
#   first_multiple(1, 5, 10)   ->  None
# ---------------------------------------------------------------------------
def first_multiple(start, stop, divisor):
    for i in range (start, stop):
        if (i % divisor == 0):
            return i
    return None


# ---------------------------------------------------------------------------
# Exercise 7: Truthy or falsy?
# Return the string "truthy" or "falsy" depending on the value.
# Do it WITHOUT comparing to specific values. Just use `if value:`
#   truthiness(0)      ->  "falsy"
#   truthiness("0")    ->  "truthy"
#   truthiness([])     ->  "falsy"
# ---------------------------------------------------------------------------
def truthiness(value):
    if value:
        return "truthy"
    else:
        return "falsy"


# ---------------------------------------------------------------------------
# Exercise 8: Day type (match)
# Use a `match` statement. Return:
#   "weekend" for "Saturday" or "Sunday"
#   "weekday" for "Monday" ... "Friday"
#   "unknown" for anything else
# ---------------------------------------------------------------------------
def day_type(day):
    match day:
        case "Saturday" | "Sunday":
            return "weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "weekday"
        case _:
            return "unknown"


# ---------------------------------------------------------------------------
# Exercise 9: Multiplication row
# PRINT the first 5 multiples of n on ONE line, separated by spaces.
# Hint: print(..., end=" ") or build up a string.
#   times_row(3) prints:
#     3 6 9 12 15
# (A trailing space before the newline is fine.)
# ---------------------------------------------------------------------------
def times_row(n):
    for i in range(1, 6):
        print(n * i, end=" ")


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
