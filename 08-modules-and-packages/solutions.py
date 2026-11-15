"""
08 - Modules and packages: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me from this folder:  python solutions.py
"""
import itertools
import json
import math
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from string_tools import slugify


def circle_area(radius):
    return math.pi * radius ** 2


def days_between(start, end):
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def most_common_letter(text):
    counts = Counter(text.replace(" ", ""))
    letter, count = counts.most_common(1)[0]
    return letter


def group_by_first_letter(words):
    groups = defaultdict(list)
    for word in words:
        groups[word[0]].append(word)
    return dict(groups)


def to_json(data):
    return json.dumps(data, sort_keys=True)


def name_from_json(text):
    return json.loads(text)["name"]


def all_pairs(items):
    return list(itertools.combinations(items, 2))


def file_extension(path):
    return Path(path).suffix


def post_url(title):
    return f"/blog/{slugify(title)}"


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
def ex01_circle_area():
    expect(circle_area(1), 3.141592653589793, "circle_area(1)")
    expect(round(circle_area(2), 4), 12.5664, "circle_area(2) (rounded)")


@check
def ex02_days_between():
    expect(days_between("2024-01-01", "2024-03-01"), 60, 'days_between("2024-01-01", "2024-03-01")')
    expect(days_between("2023-12-31", "2024-01-01"), 1, 'days_between("2023-12-31", "2024-01-01")')


@check
def ex03_most_common_letter():
    expect(most_common_letter("hello world"), "l", 'most_common_letter("hello world")')
    expect(most_common_letter("a bb  ccc"), "c", 'most_common_letter("a bb  ccc")')


@check
def ex04_group_by_first_letter():
    result = group_by_first_letter(["apple", "avocado", "banana"])
    expect(type(result).__name__, "dict", "the type of the result")
    expect(result, {"a": ["apple", "avocado"], "b": ["banana"]}, "group_by_first_letter(...)")


@check
def ex05_to_json():
    expect(to_json({"b": 1, "a": 2}), '{"a": 2, "b": 1}', 'to_json({"b": 1, "a": 2})')
    expect(to_json({"ok": True, "x": None}), '{"ok": true, "x": null}', 'to_json({"ok": True, "x": None})')


@check
def ex06_name_from_json():
    expect(name_from_json('{"name": "Ada", "age": 36}'), "Ada", "name_from_json(...)")


@check
def ex07_all_pairs():
    expect(all_pairs(["a", "b", "c"]), [("a", "b"), ("a", "c"), ("b", "c")], 'all_pairs(["a", "b", "c"])')
    expect(all_pairs([1]), [], "all_pairs([1])")


@check
def ex08_file_extension():
    expect(file_extension("reports/2024/summary.txt"), ".txt", 'file_extension("reports/2024/summary.txt")')
    expect(file_extension("README"), "", 'file_extension("README")')
    expect(file_extension("archive.tar.gz"), ".gz", 'file_extension("archive.tar.gz")')


@check
def ex09_post_url():
    expect(post_url("My First Post!"), "/blog/my-first-post", 'post_url("My First Post!")')


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
