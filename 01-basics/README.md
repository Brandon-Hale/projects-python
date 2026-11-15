# 01 · Basics

Variables, the core types, arithmetic, printing, and converting between types.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## Running Python

```bash
python examples.py     # run a file
python                 # open the interactive REPL (exit with exit())
```

There's no `Main()` method and no compile step. Python runs the file top to bottom.

## Variables

```python
name = "Ada"
age = 36
height = 1.68
is_admin = False
```

- There's no `var`, `let`, or `const`. You just assign.
- Variables have **no fixed type**. The *value* has a type, and you can reassign a different type
  (`age = "old"` is legal, though usually a bad idea).
- Naming convention is `snake_case` for variables and functions, `PascalCase` for classes,
  `UPPER_CASE` for "constants". Python doesn't enforce constants; `MAX_SIZE = 10` is just a
  promise not to change it.

> **C#/TS:** think of every variable as `dynamic`/`any`. Type hints (module 11) give you
> TypeScript-style checking back.

## Core types

| Python | Example | C# equivalent | TS equivalent |
|--------|---------|---------------|---------------|
| `int` | `42`, `-7`, `1_000_000` | `int`/`long`/`BigInteger` | `number`/`bigint` |
| `float` | `3.14`, `1e-3` | `double` | `number` |
| `str` | `"hi"`, `'hi'` | `string` | `string` |
| `bool` | `True`, `False` | `bool` | `boolean` |
| `NoneType` | `None` | `null` | `null`/`undefined` |

- `int` has **no size limit**. `2 ** 200` just works.
- Single and double quotes mean the same thing.
- `True`, `False` and `None` are **capitalised**.

Check a type with `type(x)` and test it with `isinstance(x, int)`.

## Arithmetic

```python
7 + 2    # 9
7 - 2    # 5
7 * 2    # 14
7 / 2    # 3.5    <- / ALWAYS gives a float (unlike C# int division!)
7 // 2   # 3      <- floor division (whole-number result)
7 % 2    # 1      <- remainder
7 ** 2   # 49     <- power (no Math.Pow needed)
```

There's **no `++` or `--`**. Use `count += 1`.

> **Gotcha:** `-7 // 2` is `-4` (it rounds *down*, toward negative infinity), while C# gives `-3`.

## Printing and f-strings

```python
print("Hello")                      # Hello
print("a", "b", 3)                  # a b 3   (separated by spaces)
print(f"{name} is {age} years old") # f-string = C# $"..." / TS `${}`
print(f"{height:.1f}")              # 1.7     (format spec, like C# {height:F1})
print(f"{age + 1}")                 # any expression works inside {}
```

`print` adds a newline automatically. Pass `end=""` to stop that: `print("no newline", end="")`.

## Converting between types

Python **won't** silently convert for you:

```python
"Age: " + 36          # TypeError!
"Age: " + str(36)     # "Age: 36"
int("42")             # 42
float("3.5")          # 3.5
int(3.9)              # 3   (truncates)
str(True)             # "True"
bool("")              # False  (more on this in module 02)
```

> **C#/TS:** In TS, `"5" + 1` is `"51"`. In Python it's an error. That's good, because it catches bugs.

## Multiple assignment and swapping

```python
x, y = 1, 2
x, y = y, x        # swap, no temp variable needed
a = b = 0          # both are 0
```

## Comments

```python
# Single-line comment

"""
Triple-quoted strings are often used as multi-line comments
or as documentation (docstrings, see module 03).
"""
```

## Getting input

```python
name = input("What's your name? ")   # always returns a str
age = int(input("Age? "))            # convert it yourself
```

(The exercises don't use `input()` so they can be checked automatically. Try it in the REPL.)

---

## Gotchas for C#/TS developers

1. **Indentation is syntax.** Use 4 spaces. Mixing tabs and spaces causes errors.
2. **No semicolons.** One statement per line.
3. `/` is always float division. Use `//` for integer division.
4. `True`/`False`/`None` are capitalised.
5. No implicit string conversion: `"a" + 1` is a `TypeError`.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
