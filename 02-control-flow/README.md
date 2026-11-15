# 02 · Control flow

Making decisions and repeating things: `if`, truthiness, `for`, `while`, `range`, and `match`.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## if / elif / else

```python
if temperature > 30:
    print("Hot")
elif temperature > 15:      # NOT "else if"
    print("Nice")
else:
    print("Cold")
```

- No parentheses around the condition, and no braces. The **colon + indentation** forms the block.
- An empty block needs `pass` (Python's "do nothing" statement).

### Comparisons and logic

```python
x == y   x != y   x < y   x <= y          # same as C#/TS
a and b      a or b      not a           # instead of && || !
0 < x < 10                               # chained comparison! means 0 < x and x < 10
x is None                                # identity check, the right way to test for None
```

> **TS:** There's no `===`. Python's `==` never does type coercion (`1 == "1"` is `False`).

### Ternary (conditional expression)

```python
label = "adult" if age >= 18 else "minor"     # C#/TS: age >= 18 ? "adult" : "minor"
```

## Truthiness

Any value can be used as a condition. These are **falsy**:

| Falsy value | Type |
|-------------|------|
| `False` | bool |
| `None` | NoneType |
| `0`, `0.0` | numbers |
| `""` | empty string |
| `[]`, `{}`, `set()`, `()` | empty collections |

**Everything else is truthy**, including `"0"`, `"False"`, and `[0]`.

```python
if items:              # idiomatic "if the list is not empty"
    ...
if not name:           # "if name is empty (or None)"
    ...
```

> **TS:** this is close to JS truthiness, except empty lists and dicts are **falsy** in Python.

## for loops

Python's `for` is always a **for-each**. To count, loop over a `range`:

```python
for i in range(5):           # 0, 1, 2, 3, 4      (stop is excluded)
for i in range(1, 6):        # 1, 2, 3, 4, 5
for i in range(0, 20, 5):    # 0, 5, 10, 15       (step of 5)
for i in range(10, 0, -1):   # 10, 9, ... 1       (counting down)

for letter in "abc":         # loop over a string's characters
for item in [3, 1, 2]:       # loop over a list
```

`range(1, 6)` ≈ C# `for (int i = 1; i < 6; i++)`.

## while loops

```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

There's no `do ... while`. Use `while True:` with a `break` inside instead.

## break, continue, and loop-else

```python
for n in range(10):
    if n == 3:
        continue     # skip to the next iteration
    if n == 7:
        break        # leave the loop entirely
    print(n)
```

A `for`/`while` can have an **`else`** block. It runs only if the loop finished **without**
hitting `break`. That's handy for "search, and do something if not found":

```python
for n in numbers:
    if n < 0:
        print("found a negative")
        break
else:
    print("no negatives")
```

## match (Python 3.10+)

Python's `switch`, with pattern matching similar to C# `switch` expressions:

```python
match command:
    case "start":
        print("Starting")
    case "stop" | "quit":          # multiple values
        print("Stopping")
    case _:                        # default
        print("Unknown")
```

There's no fall-through and no `break` needed. `match` can also destructure tuples, lists,
dicts and objects, but the simple form above covers most uses.

---

## Gotchas for C#/TS developers

1. `elif`, not `else if`.
2. No `for (init; cond; step)`. Use `range()`.
3. `range(a, b)` **excludes** `b`.
4. No `i++`. Use `i += 1`.
5. Empty lists, dicts and strings are falsy.
6. Use `is None` / `is not None` rather than `== None`.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
