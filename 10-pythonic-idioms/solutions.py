"""
10 - Pythonic idioms: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""
import functools
from contextlib import contextmanager


def squares(n):
    return [i * i for i in range(1, n + 1)]


def long_words_upper(words, min_length):
    return [word.upper() for word in words if len(word) > min_length]


def word_lengths(words):
    return {word: len(word) for word in words}


def flatten(nested):
    return [item for inner in nested for item in inner]


def passwords_ok(passwords):
    all_long = all(len(pw) >= 8 for pw in passwords)
    some_digit = any(any(ch.isdigit() for ch in pw) for pw in passwords)
    return all_long and some_digit


def evens_up_to(limit):
    for n in range(0, limit, 2):
        yield n
    # or: yield from range(0, limit, 2)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def by_age_desc(people):
    return sorted(people, key=lambda person: person[1], reverse=True)


def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@contextmanager
def tag(name, log):
    log.append(f"<{name}>")
    try:
        yield
    finally:
        log.append(f"</{name}>")


# =============================================================================
# CHECKS - run this file with:  python solutions.py
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
