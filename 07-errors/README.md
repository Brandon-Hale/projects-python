# 07 · Errors and exceptions

Catching, raising, and defining exceptions, plus Python's "ask forgiveness" style.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## Reading a traceback

```
Traceback (most recent call last):
  File "app.py", line 8, in <module>
    total = add_all(values)
  File "app.py", line 3, in add_all
    return sum(int(v) for v in values)
ValueError: invalid literal for int() with base 10: 'abc'
```

Read it **bottom-up**. The last line is the error type and message. The lines above show the
call chain, with the most recent call last (the opposite order to a C# stack trace).

## try / except

```python
try:
    number = int(text)
except ValueError:
    number = 0
```

> **C#/TS:** `catch` → `except`. Catch **specific** exception types, just like you would in C#.

### All the parts

```python
try:
    result = risky()
except (ValueError, TypeError) as error:   # several types, bound to a name
    print("bad input:", error)
except ZeroDivisionError:
    print("divided by zero")
else:
    print("no exception happened")         # runs only if try succeeded
finally:
    print("always runs")                   # cleanup, same as C#/TS
```

The `else` block is Python-specific. Code in it only runs when nothing was raised, which keeps
the `try` block small and focused on the line that can actually fail.

## Raising exceptions

```python
def set_age(age):
    if age < 0:
        raise ValueError("age can't be negative")   # C#: throw new ArgumentException(...)
```

Re-raise the current exception with a bare `raise` inside an `except` block:

```python
except ValueError:
    log("oops")
    raise
```

Chain exceptions with `from` to keep the original cause (like C# `InnerException`):

```python
except KeyError as error:
    raise ConfigError("missing setting") from error
```

## Common built-in exceptions

| Exception | When | C# rough equivalent |
|-----------|------|---------------------|
| `ValueError` | right type, bad value (`int("abc")`) | `ArgumentException` / `FormatException` |
| `TypeError` | wrong type (`"a" + 1`) | `InvalidCastException` / compile error |
| `KeyError` | missing dict key | `KeyNotFoundException` |
| `IndexError` | list index out of range | `IndexOutOfRangeException` |
| `AttributeError` | no such attribute/method (often on `None`) | `NullReferenceException` |
| `ZeroDivisionError` | `x / 0` | `DivideByZeroException` |
| `FileNotFoundError` | opening a missing file | `FileNotFoundException` |
| `NotImplementedError` | placeholder for unfinished code | `NotImplementedException` |

All of these inherit from `Exception`. Catching bare `Exception` catches nearly everything, so do
that only at the top level of an app (e.g. to log and exit).

## Custom exceptions

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""

class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(f"{field}: {message}")
        self.field = field
```

An empty class body with just a docstring is enough. Inherit from `Exception` (or a more
specific built-in like `ValueError`).

## EAFP vs LBYL

Python culture prefers **EAFP**: *Easier to Ask Forgiveness than Permission*.

```python
# LBYL - Look Before You Leap (common in C#)
if key in settings:
    value = settings[key]
else:
    value = default

# EAFP - just try it
try:
    value = settings[key]
except KeyError:
    value = default
```

Both are fine. EAFP avoids race conditions (e.g. a file deleted between the check and the open)
and is often cleaner. For dicts specifically, `settings.get(key, default)` beats both.

## Cleaning up with `with`

For files, locks, connections and similar resources, `with` guarantees cleanup even if an
exception is raised. It's Python's `using` statement:

```python
with open("data.txt") as f:      # C#: using (var f = File.OpenText("data.txt"))
    data = f.read()
# f is closed here, even if read() raised
```

You'll use this a lot in module 09.

---

## Gotchas for C#/TS developers

1. It's `except`, not `catch`, and `raise`, not `throw`.
2. Never write a bare `except:` with no type. It even catches Ctrl+C (`KeyboardInterrupt`).
3. Python has no checked exceptions (same as C#).
4. `AttributeError: 'NoneType' object has no attribute 'x'` is Python's NullReferenceException.
   Usually a function forgot to `return`.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
