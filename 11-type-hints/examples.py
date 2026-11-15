"""
11 - Type hints: examples
Run me:      python examples.py
Check me:    mypy examples.py      (after: pip install mypy)
"""
from collections.abc import Callable, Iterable
from dataclasses import dataclass, field
from typing import Any, Literal, Protocol, TypedDict, TypeVar, runtime_checkable


# --- Basic annotations ------------------------------------------------------------------
def greet(name: str, times: int = 1) -> str:
    return ("Hello " + name + "! ") * times


count: int = 0
ratio: float = 0.5
tags: list[str] = ["python", "typing"]
scores: dict[str, int] = {"ada": 90}
point: tuple[int, int] = (3, 4)

print("--- Basics ---")
print(greet("Ada", 2))
print("annotations live in __annotations__:", greet.__annotations__)

# Hints are NOT enforced at runtime - this line runs fine.
# mypy would report: Argument 1 to "greet" has incompatible type "int"; expected "str"
wrong: Any = 42
try:
    greet(wrong)
except TypeError as error:
    print("crashed INSIDE the function, not because of the hint:", error)


# --- Optional / unions ---------------------------------------------------------------------
USERS: dict[int, str] = {1: "ada", 2: "alan"}


def find_user(user_id: int) -> str | None:
    return USERS.get(user_id)


def describe(value: int | str) -> str:
    if isinstance(value, int):          # the checker "narrows" the type in each branch
        return f"number {value}"
    return f"text {value!r}"


print("\n--- Optional & unions ---")
user = find_user(3)
if user is None:                        # the checker makes you handle None before using it
    print("no user 3")
else:
    print(user.upper())
print(describe(5), "|", describe("five"))


# --- Callable ------------------------------------------------------------------------------------
def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)


def total_of(numbers: Iterable[float]) -> float:   # accepts list, tuple, set, generator...
    return sum(numbers)


print("\n--- Callable / Iterable ---")
print(apply(lambda x: x * 10, 4))
print(total_of([1.5, 2.5]), total_of(n / 2 for n in range(4)))


# --- Literal ----------------------------------------------------------------------------------------
Theme = Literal["light", "dark"]   # a type alias


def set_theme(theme: Theme) -> str:
    return f"theme set to {theme}"


print("\n--- Literal ---")
print(set_theme("dark"))
# set_theme("blue")   # mypy: Argument 1 has incompatible type "Literal['blue']"


# --- TypedDict -------------------------------------------------------------------------------------
class Movie(TypedDict):
    title: str
    year: int


def movie_label(movie: Movie) -> str:
    return f"{movie['title']} ({movie['year']})"


print("\n--- TypedDict ---")
dune: Movie = {"title": "Dune", "year": 2021}
print(movie_label(dune), "| still a plain dict:", type(dune).__name__)


# --- Protocol (structural typing) ---------------------------------------------------------------------
@runtime_checkable
class Greeter(Protocol):
    def greet(self) -> str: ...


class Robot:                    # doesn't inherit from Greeter...
    def greet(self) -> str:
        return "Beep boop"


class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        return f"Hi, I'm {self.name}"


class Rock:
    pass


def welcome(greeter: Greeter) -> str:
    return greeter.greet()


print("\n--- Protocol ---")
for thing in [Robot(), Person("Ada")]:
    print(welcome(thing))       # ...but both satisfy the protocol
print("Robot is a Greeter?", isinstance(Robot(), Greeter))
print("Rock is a Greeter?", isinstance(Rock(), Greeter))

# --- Generics -------------------------------------------------------------------------------------------
T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


def first(items: list[T]) -> T | None:
    return items[0] if items else None


def invert(mapping: dict[K, V]) -> dict[V, K]:
    return {value: key for key, value in mapping.items()}


print("\n--- Generics ---")
print(first([10, 20]), first(["x"]), first([]))
print(invert({"a": 1, "b": 2}))


# --- Dataclasses with types ---------------------------------------------------------------------------------
@dataclass
class User:
    name: str
    email: str | None = None
    roles: list[str] = field(default_factory=list)

    def is_admin(self) -> bool:
        return "admin" in self.roles


print("\n--- Typed dataclass ---")
admin = User("ada", roles=["admin"])
print(admin, admin.is_admin())
