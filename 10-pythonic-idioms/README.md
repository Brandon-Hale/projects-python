# 10 · Pythonic idioms

The features that make code look like *Python* rather than C# written in Python:
comprehensions, generators, `any`/`all`, unpacking, decorators, and context managers.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## List comprehensions: Python's LINQ

```python
squares = [n * n for n in range(10)]                 # Select
evens   = [n for n in numbers if n % 2 == 0]         # Where
both    = [n * n for n in numbers if n > 0]          # Where + Select
```

| C# LINQ | TS | Python |
|---------|----|--------|
| `nums.Select(n => n * 2).ToList()` | `nums.map(n => n * 2)` | `[n * 2 for n in nums]` |
| `nums.Where(n => n > 0).ToList()` | `nums.filter(n => n > 0)` | `[n for n in nums if n > 0]` |
| `nums.Any(n => n > 0)` | `nums.some(n => n > 0)` | `any(n > 0 for n in nums)` |
| `nums.All(n => n > 0)` | `nums.every(n => n > 0)` | `all(n > 0 for n in nums)` |
| `nums.Sum()` | `nums.reduce((a, b) => a + b, 0)` | `sum(nums)` |
| `nums.OrderBy(n => n.Age)` | `[...nums].sort((a, b) => ...)` | `sorted(nums, key=lambda n: n.age)` |
| `nums.SelectMany(x => x)` | `nums.flat()` | `[y for x in nums for y in x]` |
| `nums.First(n => n > 0)` | `nums.find(n => n > 0)` | `next(n for n in nums if n > 0)` |

### Dict and set comprehensions

```python
lengths = {word: len(word) for word in words}        # ToDictionary
unique_lengths = {len(word) for word in words}       # set
```

### Conditional expressions inside

```python
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
```

> **Rule of thumb:** if a comprehension doesn't fit on one or two lines, use a normal `for` loop.

## Generators: lazy sequences

A **generator expression** looks like a comprehension with round brackets. It produces values
one at a time instead of building a whole list:

```python
total = sum(n * n for n in range(1_000_000))         # no giant list in memory
```

A **generator function** uses `yield`. This is exactly C#'s `yield return` (`IEnumerable<T>`) and
TS's `function*`:

```python
def countdown(n):
    while n > 0:
        yield n           # pause here, hand back n
        n -= 1

for x in countdown(3):    # 3, 2, 1
    print(x)

list(countdown(3))        # [3, 2, 1]
```

Generators are **lazy** (nothing runs until you iterate) and **single-use**. Once exhausted,
they're empty.

## Handy built-ins and unpacking

```python
any(x > 10 for x in nums)      # at least one?
all(x > 0 for x in nums)       # every one?
max(people, key=lambda p: p.age)
first, *rest = [1, 2, 3, 4]    # first=1, rest=[2, 3, 4]
a, b = b, a                    # swap
for i, (name, score) in enumerate(zip(names, scores)): ...
merged = {**defaults, **overrides}       # merge dicts (later wins), like TS {...a, ...b}
merged = defaults | overrides            # same thing (3.9+)
combined = [*list_a, *list_b]            # like TS [...a, ...b]
_ = some_function()                      # _ means "I don't care about this value"
```

### The walrus operator `:=` (3.8+)

Assign and test in one expression:

```python
while (line := input("> ")) != "quit":
    print("you said", line)
```

## Decorators

A decorator is a function that **takes a function and returns a new (wrapped) function**.
The `@` syntax is shorthand:

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logged                 # same as: add = logged(add)
def add(a, b):
    return a + b
```

You've already used decorators: `@property`, `@classmethod`, `@staticmethod`, `@dataclass`, and
`@check` at the bottom of every exercises file! They're similar to C# attributes, except that a
decorator actually **runs code** and replaces the function.

Use `functools.wraps(func)` on your wrapper to keep the original function's name and docstring.

## Context managers: `with`

Anything usable in a `with` statement is a **context manager**. It runs setup code on entry and
**guaranteed** cleanup on exit, like C#'s `using`/`IDisposable`. The easiest way to write one:

```python
from contextlib import contextmanager

@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield                       # the body of the `with` block runs here
    finally:
        print(f"{label}: {time.perf_counter() - start:.3f}s")

with timer("work"):
    do_work()
```

## The Zen of Python

Run `import this` in the REPL. It's a short poem that explains a lot of these choices.

---

## Gotchas for C#/TS developers

1. Generators are single-use. Iterating twice gives nothing the second time.
2. `[f(x) for x in xs]` builds the whole list. Use `(f(x) for x in xs)` when you only need to loop once.
3. Don't use a comprehension just for side effects (`[print(x) for x in xs]`). Use a `for` loop.
4. Decorators run **when the function is defined**, not when it's called. The wrapper runs on each call.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
You can now read **all** of the check code at the bottom of every exercises file, so have a look!
