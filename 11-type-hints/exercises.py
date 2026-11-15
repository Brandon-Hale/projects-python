"""
11 - Type hints: exercises

The checks look at your ANNOTATIONS as well as the results, so for each
exercise:
  1. add the type hints described,
  2. delete the `raise NotImplementedError` line and write the code.

Run:  python exercises.py
Extra credit:  pip install mypy  then  mypy exercises.py
"""
from collections.abc import Callable
from typing import Protocol, TypedDict, TypeVar, runtime_checkable

T = TypeVar("T")


# ---------------------------------------------------------------------------
# Exercise 1: Basic hints
# Both parameters are ints, and it returns an int (their sum).
#   add(2, 3)  ->  5
# ---------------------------------------------------------------------------
def add(a, b):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: Collections
# `words` is a list of strings, `sep` is a string defaulting to " ".
# Returns a string: the words joined by sep.
#   join_words(["a", "b"])        ->  "a b"
#   join_words(["a", "b"], "-")   ->  "a-b"
# ---------------------------------------------------------------------------
def join_words(words, sep=" "):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: Optional return
# `users` maps int ids to str names. `user_id` is an int.
# Return the name, or None if the id isn't there.
# The return type should say "a str OR None".
#   find_user({1: "ada"}, 1)  ->  "ada"
#   find_user({1: "ada"}, 2)  ->  None
# ---------------------------------------------------------------------------
def find_user(users, user_id):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: Callable
# `func` takes an int and returns an int. `value` is an int.
# Return func(value). (Callable is already imported above.)
#   apply(lambda x: x * 2, 21)  ->  42
# ---------------------------------------------------------------------------
def apply(func, value):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: Generics
# `items` is a list of T (T is defined above). Return the LAST item, or
# None if the list is empty. Return type: T or None.
#   last([1, 2, 3])  ->  3
#   last([])         ->  None
# ---------------------------------------------------------------------------
def last(items):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: TypedDict
# Give the Movie TypedDict two fields: title (str) and year (int).
# Then write movie_label: takes a Movie, returns a str like "Dune (2021)".
# ---------------------------------------------------------------------------
class Movie(TypedDict):
    pass  # replace this with the two fields


def movie_label(movie):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Protocol
# Greeter is a protocol (an interface). Write a class Robot that satisfies
# it WITHOUT inheriting from it: give Robot a greet method, annotated to
# return str, that returns "Beep boop".
# ---------------------------------------------------------------------------
@runtime_checkable
class Greeter(Protocol):
    def greet(self) -> str: ...


class Robot:
    def greet(self):
        raise NotImplementedError  # delete this line and write your code


# =============================================================================
# CHECKS - run this file with:  python exercises.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
import types
import typing
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


def _normalise(hint):
    """Make equivalent spellings compare equal: Optional[str] == str | None, List[int] == list[int]."""
    if isinstance(hint, list):
        return tuple(_normalise(h) for h in hint)
    origin = typing.get_origin(hint)
    if origin is None:
        return hint
    args = typing.get_args(hint)
    if origin in (typing.Union, types.UnionType):
        return ("union", frozenset(_normalise(a) for a in args))
    return (origin, tuple(_normalise(a) for a in args))


def expect_hints(obj, expected):
    try:
        hints = typing.get_type_hints(obj)
    except Exception as error:
        raise AssertionError(f"couldn't read the type hints: {error}")
    for name, hint in expected.items():
        where = "return type" if name == "return" else f"hint for {name!r}"
        assert name in hints, f"missing the {where} on {obj.__name__}"
        assert _normalise(hints[name]) == _normalise(hint), \
            f"the {where} on {obj.__name__} should be {hint!r}, got {hints[name]!r}"


@check
def ex01_add():
    expect(add(2, 3), 5, "add(2, 3)")
    expect_hints(add, {"a": int, "b": int, "return": int})


@check
def ex02_join_words():
    expect(join_words(["a", "b"]), "a b", 'join_words(["a", "b"])')
    expect(join_words(["a", "b"], "-"), "a-b", 'join_words(["a", "b"], "-")')
    expect_hints(join_words, {"words": list[str], "sep": str, "return": str})


@check
def ex03_find_user():
    expect(find_user({1: "ada"}, 1), "ada", 'find_user({1: "ada"}, 1)')
    expect(find_user({1: "ada"}, 2), None, 'find_user({1: "ada"}, 2)')
    expect_hints(find_user, {"users": dict[int, str], "user_id": int, "return": str | None})


@check
def ex04_apply():
    expect(apply(lambda x: x * 2, 21), 42, "apply(lambda x: x * 2, 21)")
    expect_hints(apply, {"func": Callable[[int], int], "value": int, "return": int})


@check
def ex05_last():
    expect(last([1, 2, 3]), 3, "last([1, 2, 3])")
    expect(last([]), None, "last([])")
    expect_hints(last, {"items": list[T], "return": T | None})


@check
def ex06_movie():
    expect(movie_label({"title": "Dune", "year": 2021}), "Dune (2021)", "movie_label(...)")
    expect(typing.get_type_hints(Movie), {"title": str, "year": int}, "Movie's fields")
    expect_hints(movie_label, {"movie": Movie, "return": str})


@check
def ex07_robot():
    expect(Robot().greet(), "Beep boop", "Robot().greet()")
    assert Greeter not in Robot.__mro__, "Robot shouldn't inherit from Greeter - that's the point of a Protocol!"
    assert isinstance(Robot(), Greeter), "Robot should satisfy the Greeter protocol"
    expect_hints(Robot.greet, {"return": str})


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
