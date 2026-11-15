"""
04 - Collections: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def last_three(items):
    return items[-3:]   # slicing never goes out of range - it just gives what's there


def reverse_list(items):
    return items[::-1]  # or: list(reversed(items))


def count_words(words):
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
    # In module 08 you'll meet collections.Counter, which does this for you.


def unique_sorted(items):
    return sorted(set(items))   # set removes duplicates, sorted returns a list


def common_items(a, b):
    return sorted(set(a) & set(b))


def pair_up(names, scores):
    return dict(zip(names, scores))


def numbered(items):
    result = []
    for i, item in enumerate(items, start=1):
        result.append(f"{i}. {item}")
    return result


def invert(mapping):
    result = {}
    for key, value in mapping.items():
        result[value] = key
    return result


def oldest(people):
    name, age = max(people, key=lambda person: person[1])
    return name


def lookup(phone_book, name):
    return phone_book.get(name, "unknown")


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
