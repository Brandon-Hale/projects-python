# 11 · Type hints

TypeScript-style static types for Python: annotations, generics, `Optional`, `Callable`,
`TypedDict`, `Protocol`, and running a type checker.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## The big idea

```python
def greet(name: str, times: int = 1) -> str:
    return ("Hello " + name + "! ") * times

age: int = 36
```

Type hints are **not enforced at runtime**. Python ignores them when running your code:

```python
greet(42)       # runs (and crashes inside on "Hello " + 42), with no error from the hint itself
```

They're for **tools**: your editor (autocomplete, red squiggles) and a **type checker** like
`mypy` or `pyright` (which powers VS Code's Pylance). If you know TypeScript, this is exactly the
same deal: types are checked before running and erased at runtime.

## Running a type checker

```bash
pip install mypy          # (inside a virtual environment, see module 08)
mypy examples.py
```

In VS Code, set **Python › Analysis: Type Checking Mode** to `basic` or `strict` to see errors live.

## Basic types

```python
count: int = 0
price: float = 9.99          # an int is accepted where a float is expected
name: str = "Ada"
active: bool = True
data: bytes = b"\x00"
nothing: None = None
```

## Collections (built-in generics, 3.9+)

```python
names: list[str] = []
scores: dict[str, int] = {}
unique: set[int] = set()
point: tuple[int, int] = (3, 4)            # fixed length
values: tuple[int, ...] = (1, 2, 3)        # any length
```

| TypeScript | Python |
|-----------|--------|
| `string[]` | `list[str]` |
| `Record<string, number>` | `dict[str, int]` |
| `[number, number]` | `tuple[int, int]` |
| `string \| null` | `str \| None` (or `Optional[str]`) |
| `string \| number` | `str \| int` |
| `any` | `Any` |
| `unknown` | `object` |
| `(x: number) => string` | `Callable[[int], str]` |
| `"red" \| "green"` | `Literal["red", "green"]` |
| `interface` (structural) | `Protocol` |
| `type User = { name: string }` | `TypedDict` |
| `function first<T>(xs: T[]): T` | `def first(xs: list[T]) -> T` with `T = TypeVar("T")` |

## Optional and unions

```python
def find(user_id: int) -> str | None:      # may return None (3.10+ syntax)
    ...

from typing import Optional
def find(user_id: int) -> Optional[str]:   # older, equivalent spelling
    ...
```

The checker then forces you to handle `None`, just like TS strict null checks.

## Functions as values

```python
from collections.abc import Callable

def apply(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

## Literal, Any, Final

```python
from typing import Any, Final, Literal

def set_mode(mode: Literal["light", "dark"]) -> None: ...
def log(value: Any) -> None: ...              # opt out of checking
MAX_SIZE: Final = 100                          # checker complains if reassigned
```

## TypedDict: typing dict "shapes"

```python
from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int

m: Movie = {"title": "Dune", "year": 2021}    # it's still a normal dict at runtime
```

Prefer a `@dataclass` for your own data. Use `TypedDict` to describe dicts you get from JSON, APIs, etc.

## Protocol: interfaces, TypeScript-style

A `Protocol` is a **structural** interface. Any class with matching methods satisfies it, with no
`implements` or inheritance needed. That's exactly how TS interfaces work (and unlike C#'s
nominal interfaces):

```python
from typing import Protocol

class Greeter(Protocol):
    def greet(self) -> str: ...

class Robot:                       # never mentions Greeter!
    def greet(self) -> str:
        return "Beep boop"

def welcome(g: Greeter) -> None:
    print(g.greet())

welcome(Robot())                   # type checks fine
```

Add `@runtime_checkable` to the protocol if you also want `isinstance(x, Greeter)` to work.

## Generics

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T | None:
    return items[0] if items else None

first([1, 2, 3])     # checker knows this is int | None
first(["a"])         # str | None
```

Python 3.12+ adds a shorter syntax: `def first[T](items: list[T]) -> T | None:`.
This course sticks to `TypeVar` so it works on 3.10+.

## Classes

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    email: str | None = None
    tags: list[str] = field(default_factory=list)

    def display(self) -> str: ...
```

Use a class's name as a type: `def save(user: User) -> None`. For a method returning its own
class, use `from typing import Self` (3.11+) or quote the name: `-> "User"`.

---

## Gotchas for C#/TS developers

1. Hints aren't enforced at runtime. You need mypy/pyright to get errors.
2. `list[int]` (lowercase) is the modern spelling. `List[int]` from `typing` is the old one.
3. A function with no return annotation is treated as untyped by mypy unless you use `--strict`.
4. `Optional[X]` means "X or None". It does **not** mean the argument is optional; that's what
   a default value does.

## Your turn

Open [`exercises.py`](exercises.py). The checks look at your **annotations** as well as the
results, so write the hints too! Run `python exercises.py`. For extra credit, run `mypy exercises.py`.
