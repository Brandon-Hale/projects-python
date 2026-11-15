"""
08 - Modules and packages: exercises

Each exercise asks you to use a STANDARD LIBRARY module. Put your imports
at the top of this file (just below this docstring) or inside the function.

Delete each `raise NotImplementedError` line, write your code,
then run from this folder:  python exercises.py
"""

# Put your imports here, e.g.:
# import math


# ---------------------------------------------------------------------------
# Exercise 1: math
# Return the area of a circle with the given radius, using math.pi.
#   circle_area(1)  ->  3.141592653589793
# ---------------------------------------------------------------------------
def circle_area(radius):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: datetime
# Both arguments are dates as "YYYY-MM-DD" strings. Return the number of
# days from the first to the second as an int.
# Hint: date.fromisoformat(...), then subtract and use .days
#   days_between("2024-01-01", "2024-03-01")  ->  60
# ---------------------------------------------------------------------------
def days_between(start, end):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: collections.Counter
# Return the most common letter in the text (ignore spaces).
#   most_common_letter("hello world")  ->  "l"
# ---------------------------------------------------------------------------
def most_common_letter(text):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: collections.defaultdict
# Group words by their first letter. Return a normal dict.
#   group_by_first_letter(["apple", "avocado", "banana"])
#     ->  {"a": ["apple", "avocado"], "b": ["banana"]}
# ---------------------------------------------------------------------------
def group_by_first_letter(words):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: json
# Convert a dict to a JSON string with the keys SORTED.
#   to_json({"b": 1, "a": 2})  ->  '{"a": 2, "b": 1}'
# ---------------------------------------------------------------------------
def to_json(data):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: json (the other way)
# Parse a JSON string and return the value stored under "name".
#   name_from_json('{"name": "Ada", "age": 36}')  ->  "Ada"
# ---------------------------------------------------------------------------
def name_from_json(text):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: itertools
# Return a list of every possible PAIR from items (order doesn't matter,
# no repeats) as tuples.
#   all_pairs(["a", "b", "c"])  ->  [("a", "b"), ("a", "c"), ("b", "c")]
# ---------------------------------------------------------------------------
def all_pairs(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: pathlib
# Return the file extension of a path, including the dot.
#   file_extension("reports/2024/summary.txt")  ->  ".txt"
#   file_extension("README")                    ->  ""
# ---------------------------------------------------------------------------
def file_extension(path):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 9: Your own module
# string_tools.py in this folder has a slugify() function.
# Import it and use it to return the slug of a blog post title.
#   post_url("My First Post!")  ->  "/blog/my-first-post"
# ---------------------------------------------------------------------------
def post_url(title):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Bonus (no automatic check):
#   1. Create a new file in this folder called my_utils.py with a function
#      `double(n)` that returns n * 2.
#   2. Import it in the Python REPL (run `python` in this folder) and call it.
#   3. Add an `if __name__ == "__main__":` block to my_utils.py that prints
#      something. Notice it runs with `python my_utils.py` but NOT on import.
#   4. Make a virtual environment, activate it, and `pip install requests`.
# ---------------------------------------------------------------------------


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
