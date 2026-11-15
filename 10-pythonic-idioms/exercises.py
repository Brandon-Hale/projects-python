"""
10 - Pythonic idioms: exercises

Most of these can be ONE line. Try to use comprehensions, generators and
built-ins rather than writing out full loops.

Delete each `raise NotImplementedError` line, write your code,
then run:  python exercises.py
"""
import functools
from contextlib import contextmanager


# ---------------------------------------------------------------------------
# Exercise 1: Squares (list comprehension)
# Return a list of the squares of 1..n.
#   squares(4)  ->  [1, 4, 9, 16]
# ---------------------------------------------------------------------------
def squares(n):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: Filter (list comprehension with if)
# Return only the words longer than `min_length`, in UPPER case.
#   long_words_upper(["hi", "hello", "hey", "howdy"], 3)  ->  ["HELLO", "HOWDY"]
# ---------------------------------------------------------------------------
def long_words_upper(words, min_length):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: Dict comprehension
# Map each word to its length.
#   word_lengths(["a", "abc"])  ->  {"a": 1, "abc": 3}
# ---------------------------------------------------------------------------
def word_lengths(words):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: Flatten
# Turn a list of lists into a single list (nested comprehension).
#   flatten([[1, 2], [3], [], [4, 5]])  ->  [1, 2, 3, 4, 5]
# ---------------------------------------------------------------------------
def flatten(nested):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: any / all
# Return True if EVERY password is at least 8 characters AND at least one
# of them contains a digit.
# Hint: all(...) and any(...) with generator expressions;
#       any(ch.isdigit() for ch in pw) tells you if pw has a digit.
# ---------------------------------------------------------------------------
def passwords_ok(passwords):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: Generator function
# YIELD the even numbers from 0 up to (but not including) limit.
#   list(evens_up_to(7))  ->  [0, 2, 4, 6]
# (It must use `yield` - the check makes sure it's a generator.)
# ---------------------------------------------------------------------------
def evens_up_to(limit):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Infinite generator
# YIELD the Fibonacci numbers forever: 0, 1, 1, 2, 3, 5, 8, ...
# (The check only takes the first few, so infinite is fine.)
# ---------------------------------------------------------------------------
def fibonacci():
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: Sort with a key
# Sort people (a list of (name, age) tuples) by age, OLDEST first.
#   by_age_desc([("a", 30), ("b", 50), ("c", 40)])
#     ->  [("b", 50), ("c", 40), ("a", 30)]
# ---------------------------------------------------------------------------
def by_age_desc(people):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 9: Decorator
# Write a decorator `uppercase` that makes a function's (string) return
# value UPPER case. Use @functools.wraps(func) on your wrapper.
#
#   @uppercase
#   def greet(name):
#       return f"hello {name}"
#
#   greet("ada")  ->  "HELLO ADA"
# ---------------------------------------------------------------------------
def uppercase(func):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 10: Context manager
# Write a context manager `tag(name, log)` that appends "<name>" to the log
# list on entry, and "</name>" on exit - even if the block raises.
#
#   log = []
#   with tag("b", log):
#       log.append("bold text")
#   log  ->  ["<b>", "bold text", "</b>"]
#
# Use the @contextmanager decorator (already imported) and `yield`.
# ---------------------------------------------------------------------------
@contextmanager
def tag(name, log):
    raise NotImplementedError  # delete this line and write your code
    yield


# =============================================================================
# CHECKS - run this file with:  python exercises.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import inspect
import io
import itertools
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
def ex01_squares():
    expect(squares(4), [1, 4, 9, 16], "squares(4)")
    expect(squares(0), [], "squares(0)")


@check
def ex02_long_words_upper():
    expect(long_words_upper(["hi", "hello", "hey", "howdy"], 3), ["HELLO", "HOWDY"],
           'long_words_upper(["hi", "hello", "hey", "howdy"], 3)')


@check
def ex03_word_lengths():
    expect(word_lengths(["a", "abc"]), {"a": 1, "abc": 3}, 'word_lengths(["a", "abc"])')


@check
def ex04_flatten():
    expect(flatten([[1, 2], [3], [], [4, 5]]), [1, 2, 3, 4, 5], "flatten([[1, 2], [3], [], [4, 5]])")


@check
def ex05_passwords_ok():
    expect(passwords_ok(["longenough", "password1"]), True, 'passwords_ok(["longenough", "password1"])')
    expect(passwords_ok(["longenough", "short1"]), False, 'passwords_ok(["longenough", "short1"])')
    expect(passwords_ok(["nodigitshere", "stillnodigits"]), False,
           'passwords_ok(["nodigitshere", "stillnodigits"])')


@check
def ex06_evens_up_to():
    result = evens_up_to(7)
    assert inspect.isgenerator(result), "evens_up_to should be a generator function (use yield)"
    expect(list(result), [0, 2, 4, 6], "list(evens_up_to(7))")


@check
def ex07_fibonacci():
    result = fibonacci()
    assert inspect.isgenerator(result), "fibonacci should be a generator function (use yield)"
    expect(list(itertools.islice(result, 10)), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34],
           "the first 10 values of fibonacci()")


@check
def ex08_by_age_desc():
    expect(by_age_desc([("a", 30), ("b", 50), ("c", 40)]), [("b", 50), ("c", 40), ("a", 30)],
           'by_age_desc([("a", 30), ("b", 50), ("c", 40)])')


@check
def ex09_uppercase():
    @uppercase
    def greet(name):
        """Say hello."""
        return f"hello {name}"

    assert callable(greet), "uppercase(func) should return a function"
    expect(greet("ada"), "HELLO ADA", 'greet("ada")')
    expect(greet.__name__, "greet", "the decorated function's __name__ (did you use functools.wraps?)")


@check
def ex10_tag():
    log = []
    with tag("b", log):
        log.append("bold text")
    expect(log, ["<b>", "bold text", "</b>"], "the log")

    log = []
    try:
        with tag("i", log):
            raise ValueError("boom")
    except ValueError:
        pass
    else:
        raise AssertionError("the ValueError should not be swallowed")
    expect(log, ["<i>", "</i>"], "the log when the block raises")


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
