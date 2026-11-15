# 05 · Strings

Working with text: methods, slicing, formatting, `split`/`join`, and a few handy tricks.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## Creating strings

```python
a = 'single'
b = "double"                     # same thing
c = """triple quotes
can span lines"""
path = r"C:\new\folder"          # raw string: backslashes aren't escapes (like C# @"...")
```

Strings are **immutable**, just like C# and TS. Every method returns a **new** string.

## There's no `char` type

A single character is simply a string of length 1. Indexing gives you strings:

```python
word = "python"
word[0]       # "p"
word[-1]      # "n"
word[1:4]     # "yth"     (slicing, same rules as lists)
word[::-1]    # "nohtyp"  (reverse)
len(word)     # 6
"th" in word  # True      (substring check, like .Contains / .includes)

ord("A")      # 65   char -> code point
chr(65)       # "A"  code point -> char
```

## Common methods

| Python | C# | TS |
|--------|----|----|
| `s.upper()` / `s.lower()` | `ToUpper()` / `ToLower()` | `toUpperCase()` / `toLowerCase()` |
| `s.strip()` | `Trim()` | `trim()` |
| `s.lstrip()` / `s.rstrip()` | `TrimStart()` / `TrimEnd()` | `trimStart()` / `trimEnd()` |
| `s.split(",")` | `Split(',')` | `split(",")` |
| `", ".join(items)` | `string.Join(", ", items)` | `items.join(", ")` |
| `s.replace("a", "b")` | `Replace("a", "b")` | `replaceAll("a", "b")` |
| `s.startswith("x")` | `StartsWith("x")` | `startsWith("x")` |
| `s.endswith("x")` | `EndsWith("x")` | `endsWith("x")` |
| `s.find("x")` | `IndexOf("x")` | `indexOf("x")` |
| `s.count("x")` | n/a | n/a |
| `s.title()` / `s.capitalize()` | n/a | n/a |
| `s.isdigit()` / `s.isalpha()` / `s.isspace()` | `char.IsDigit` etc. | regex |
| `s.zfill(5)` / `s.ljust(10)` / `s.center(10)` | `PadLeft` / `PadRight` | `padStart` / `padEnd` |

Note that **`join` is a method on the separator**, not on the list. `", ".join(["a", "b"])` gives `"a, b"`.
Every item must already be a string, so use `", ".join(str(n) for n in numbers)` for numbers.

`split()` with **no argument** splits on any run of whitespace and drops empty strings:

```python
"  hello   world ".split()     # ["hello", "world"]
"a,b,,c".split(",")            # ["a", "b", "", "c"]
```

## f-string formatting

```python
name, price, qty = "Widget", 1234.5, 7
f"{name}"            # Widget
f"{price:.2f}"       # 1234.50     (2 decimal places)
f"{price:,.2f}"      # 1,234.50    (thousands separator)
f"{qty:03}"          # 007         (zero pad to width 3)
f"{name:>10}"        # '    Widget' (right align in 10)
f"{name:<10}|"       # 'Widget    |' (left align)
f"{name:^10}"        # '  Widget  ' (centre)
f"{0.256:.1%}"       # 25.6%
f"{name!r}"          # 'Widget'    (repr: shows quotes, useful for debugging)
f"{qty=}"            # qty=7       (handy debug shortcut)
```

> **C#:** `{price:N2}` → `{price:,.2f}`. **TS:** use `toFixed`/`Intl` in JS, or a format spec here.

## Building strings efficiently

Use `join` instead of `+=` in a loop. It's cleaner and faster:

```python
parts = []
for n in range(5):
    parts.append(str(n))
result = "-".join(parts)   # "0-1-2-3-4"
```

(This is the Python equivalent of reaching for `StringBuilder`.)

## Looping over a string

```python
for ch in "hey":
    print(ch)

for i, ch in enumerate("hey"):
    print(i, ch)
```

## str() vs repr()

`str(x)` is the friendly version for users. `repr(x)` is the unambiguous version for developers:

```python
str("hi")    # hi
repr("hi")   # 'hi'
```

---

## Gotchas for C#/TS developers

1. There's no `char`. `"abc"[0]` is the string `"a"`.
2. `join` is `separator.join(list)`, which feels backwards at first.
3. `replace` replaces **all** occurrences by default (unlike JS `replace`).
4. Strings are immutable. `s.upper()` doesn't change `s`, so you need `s = s.upper()`.
5. `"5" * 3` is `"555"`. Repetition is a feature!

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
