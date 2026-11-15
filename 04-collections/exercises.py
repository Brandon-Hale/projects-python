"""
04 - Collections: exercises

Delete each `raise NotImplementedError` line, write your code,
then run:  python exercises.py
"""


# ---------------------------------------------------------------------------
# Exercise 1: Last three
# Return the last three items of a list using SLICING.
# (If the list has fewer than three items, return all of them.)
#   last_three([1, 2, 3, 4, 5])  ->  [3, 4, 5]
# ---------------------------------------------------------------------------
def last_three(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: Reversed copy
# Return a NEW list in reverse order. Don't change the original list!
#   reverse_list([1, 2, 3])  ->  [3, 2, 1]
# ---------------------------------------------------------------------------
def reverse_list(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: Count words
# Return a dict mapping each word to how many times it appears.
#   count_words(["a", "b", "a"])  ->  {"a": 2, "b": 1}
# ---------------------------------------------------------------------------
def count_words(words):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: Unique and sorted
# Return a sorted LIST with duplicates removed.
#   unique_sorted([3, 1, 3, 2, 1])  ->  [1, 2, 3]
# ---------------------------------------------------------------------------
def unique_sorted(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: Common items
# Return a sorted list of the items that appear in BOTH lists (no duplicates).
# Hint: sets!
#   common_items([1, 2, 3, 4], [3, 4, 5])  ->  [3, 4]
# ---------------------------------------------------------------------------
def common_items(a, b):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: Pair up
# Given a list of names and a list of scores (same length), return a dict
# mapping each name to its score.
#   pair_up(["ada", "alan"], [90, 85])  ->  {"ada": 90, "alan": 85}
# ---------------------------------------------------------------------------
def pair_up(names, scores):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Numbered list
# Return a list of strings numbering each item, starting from 1.
# Use enumerate.
#   numbered(["eggs", "milk"])  ->  ["1. eggs", "2. milk"]
# ---------------------------------------------------------------------------
def numbered(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: Invert a dict
# Swap keys and values.
#   invert({"a": 1, "b": 2})  ->  {1: "a", 2: "b"}
# ---------------------------------------------------------------------------
def invert(mapping):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 9: Oldest person
# `people` is a list of (name, age) tuples. Return the NAME of the oldest.
# Hint: max() with key=..., then unpack the tuple.
#   oldest([("ada", 36), ("grace", 85), ("alan", 41)])  ->  "grace"
# ---------------------------------------------------------------------------
def oldest(people):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 10: Safe lookup
# Return the phone number for `name` from the `phone_book` dict, or the
# string "unknown" if the name isn't there. Don't let it raise KeyError!
#   lookup({"ada": "555-1234"}, "ada")  ->  "555-1234"
#   lookup({"ada": "555-1234"}, "bob")  ->  "unknown"
# ---------------------------------------------------------------------------
def lookup(phone_book, name):
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
def ex01_last_three():
    expect(last_three([1, 2, 3, 4, 5]), [3, 4, 5], "last_three([1, 2, 3, 4, 5])")
    expect(last_three([1, 2]), [1, 2], "last_three([1, 2])")


@check
def ex02_reverse_list():
    original = [1, 2, 3]
    expect(reverse_list(original), [3, 2, 1], "reverse_list([1, 2, 3])")
    expect(original, [1, 2, 3], "The original list (it should not change)")


@check
def ex03_count_words():
    expect(count_words(["a", "b", "a"]), {"a": 2, "b": 1}, 'count_words(["a", "b", "a"])')
    expect(count_words([]), {}, "count_words([])")


@check
def ex04_unique_sorted():
    expect(unique_sorted([3, 1, 3, 2, 1]), [1, 2, 3], "unique_sorted([3, 1, 3, 2, 1])")
    expect(unique_sorted(["b", "a", "b"]), ["a", "b"], 'unique_sorted(["b", "a", "b"])')


@check
def ex05_common_items():
    expect(common_items([1, 2, 3, 4], [3, 4, 5]), [3, 4], "common_items([1, 2, 3, 4], [3, 4, 5])")
    expect(common_items([1, 1, 2], [1, 1]), [1], "common_items([1, 1, 2], [1, 1])")
    expect(common_items([1], [2]), [], "common_items([1], [2])")


@check
def ex06_pair_up():
    expect(pair_up(["ada", "alan"], [90, 85]), {"ada": 90, "alan": 85},
           'pair_up(["ada", "alan"], [90, 85])')


@check
def ex07_numbered():
    expect(numbered(["eggs", "milk"]), ["1. eggs", "2. milk"], 'numbered(["eggs", "milk"])')
    expect(numbered([]), [], "numbered([])")


@check
def ex08_invert():
    expect(invert({"a": 1, "b": 2}), {1: "a", 2: "b"}, 'invert({"a": 1, "b": 2})')


@check
def ex09_oldest():
    people = [("ada", 36), ("grace", 85), ("alan", 41)]
    expect(oldest(people), "grace", "oldest(...)")


@check
def ex10_lookup():
    book = {"ada": "555-1234"}
    expect(lookup(book, "ada"), "555-1234", 'lookup(book, "ada")')
    expect(lookup(book, "bob"), "unknown", 'lookup(book, "bob")')


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
