"""
11 - Type hints: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""
from collections.abc import Callable
from typing import Protocol, TypedDict, TypeVar, runtime_checkable

T = TypeVar("T")


def add(a: int, b: int) -> int:
    return a + b


def join_words(words: list[str], sep: str = " ") -> str:
    return sep.join(words)


def find_user(users: dict[int, str], user_id: int) -> str | None:
    return users.get(user_id)


def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)


def last(items: list[T]) -> T | None:
    return items[-1] if items else None


class Movie(TypedDict):
    title: str
    year: int


def movie_label(movie: Movie) -> str:
    return f"{movie['title']} ({movie['year']})"


@runtime_checkable
class Greeter(Protocol):
    def greet(self) -> str: ...


class Robot:
    def greet(self) -> str:
        return "Beep boop"


# =============================================================================
# CHECKS - run this file with:  python solutions.py
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
