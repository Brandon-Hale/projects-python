# 03 · Functions

Defining functions, parameters of every flavour, returning multiple values, closures, and lambdas.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## Defining and calling

```python
def greet(name):
    """Return a friendly greeting."""     # docstring, like C# /// <summary>
    return f"Hello, {name}"

message = greet("Ada")
```

- A function without `return` (or with a bare `return`) returns `None`.
- Functions must be **defined before they're called** at runtime. Python runs top to bottom,
  so the `def` line has to execute first.
- Functions can live at the top level of a file. They don't need a class.

## Default parameter values

```python
def power(base, exponent=2):
    return base ** exponent

power(3)       # 9
power(3, 3)    # 27
```

## Keyword arguments

Any parameter can be passed **by name**, in any order. This is like C# named arguments:

```python
power(exponent=3, base=2)   # 8
```

Put a bare `*` in the parameter list to make everything after it **keyword-only**:

```python
def connect(host, *, timeout=30, retries=3):
    ...

connect("example.com", timeout=5)    # OK
connect("example.com", 5)            # TypeError: timeout must be named
```

## *args and **kwargs

```python
def total(*numbers):          # collects extra positional args into a tuple
    return sum(numbers)       # like C# `params int[] numbers` / TS `...numbers`

total(1, 2, 3)                # 6

def show(**options):          # collects extra keyword args into a dict
    for key, value in options.items():
        print(key, "=", value)

show(colour="red", size=3)
```

The names `args` and `kwargs` are just convention. The `*` and `**` are what matter.

They also work in reverse, to **spread** values into a call:

```python
nums = [1, 2, 3]
total(*nums)                  # same as total(1, 2, 3)  (like TS ...spread)

settings = {"timeout": 5}
connect("example.com", **settings)
```

## Returning multiple values

```python
def min_max(numbers):
    return min(numbers), max(numbers)   # really returns ONE tuple

low, high = min_max([3, 1, 4])          # unpack it
```

> **C#:** like returning a value tuple `(int, int)` and deconstructing it.

## Functions are values

```python
def shout(text):
    return text.upper()

speak = shout          # no () means we're referencing the function, not calling it
speak("hi")            # "HI"

def apply(func, value):
    return func(value)

apply(shout, "hey")    # "HEY"
```

> **C#:** like passing a `Func<string, string>`. **TS:** exactly like passing a function.

## Lambdas

Short anonymous functions, limited to **a single expression**:

```python
double = lambda x: x * 2              # C#/TS: x => x * 2
sorted(words, key=lambda w: len(w))   # most common use: as a key/callback
```

For anything more than one expression, write a normal `def`. (Lambdas can't contain statements.)

## Closures

Inner functions can see variables from the outer function:

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count         # needed to REASSIGN an outer variable
        count += 1
        return count
    return increment

counter = make_counter()
counter()   # 1
counter()   # 2
```

`nonlocal` is for an enclosing function's variable, and `global` is for a module-level variable.
You only need them when you **assign** to the variable. Reading it works without them.

## ⚠️ The mutable default argument trap

Default values are created **once**, when the function is defined, not on each call:

```python
def add_item(item, items=[]):     # BUG: the same list is shared between calls!
    items.append(item)
    return items

add_item("a")   # ['a']
add_item("b")   # ['a', 'b']   <- surprise!
```

The fix is to use `None` as the default and create the list inside:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## Gotchas for C#/TS developers

1. No overloading. Define a function twice and the second replaces the first. Use default
   values or `*args` instead.
2. Never use mutable defaults (`[]`, `{}`). Use `None`.
3. Lambdas are one expression only.
4. Forgetting `return` gives you `None`. That's a common source of `'NoneType' object has no attribute...` errors.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
