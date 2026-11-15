# 09 · Files and I/O

Reading and writing text files, the `with` statement, `pathlib`, and the CSV and JSON formats.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)
· sample data: [`data/poem.txt`](data/poem.txt), [`data/sales.csv`](data/sales.csv)

---

## Opening files with `with`

```python
with open("notes.txt", encoding="utf-8") as f:   # C#: using var f = File.OpenText(...)
    text = f.read()
# the file is closed automatically here, even if an exception happened
```

**Always use `with`** and **always pass `encoding="utf-8"`**. Without it, Windows may default to
a legacy encoding and mangle non-ASCII characters.

### Modes

| Mode | Meaning |
|------|---------|
| `"r"` | read (default). Error if missing |
| `"w"` | write. **Creates or overwrites** |
| `"a"` | append. Creates if missing |
| `"x"` | create. Error if it already exists |
| `"rb"` / `"wb"` | binary read/write (images, zips...) |

## Reading

```python
with open(path, encoding="utf-8") as f:
    whole = f.read()              # entire file as one string

with open(path, encoding="utf-8") as f:
    lines = f.readlines()         # list of lines, each still ending in "\n"

with open(path, encoding="utf-8") as f:
    for line in f:                # streams line by line (best for big files)
        print(line.rstrip("\n"))

lines = whole.splitlines()        # split into lines WITHOUT the "\n"
```

## Writing

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")        # write() does NOT add a newline for you
    f.writelines(["a\n", "b\n"])
    print("also works", file=f)    # print() can target a file too
```

## pathlib: modern paths

`pathlib.Path` is the modern, object-oriented way to work with paths. It's like `System.IO.Path`,
`File` and `Directory` rolled into one object:

```python
from pathlib import Path

folder = Path("data")
file = folder / "notes.txt"          # join with /  (works on Windows too)

file.exists()
file.read_text(encoding="utf-8")     # quick read: File.ReadAllText
file.write_text("hi", encoding="utf-8")
file.name, file.stem, file.suffix    # "notes.txt", "notes", ".txt"
file.parent                          # Path("data")

folder.mkdir(parents=True, exist_ok=True)  # Directory.CreateDirectory
list(folder.glob("*.txt"))           # files matching a pattern
list(folder.rglob("*.py"))           # ...recursively
file.unlink(missing_ok=True)         # delete a file

Path(__file__).parent                # the folder of the CURRENT script
```

> **Tip:** `Path(__file__).parent / "data" / "poem.txt"` finds files next to your script no matter
> which folder you run it from.

## CSV

```python
import csv

with open("sales.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):            # each row is a dict keyed by the header
        print(row["product"], row["amount"]) # values are always STRINGS

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    writer.writerows([["ada", 90], ["alan", 85]])
```

Pass `newline=""` when opening CSV files. It stops blank lines appearing between rows on Windows.

## JSON files

```python
import json

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)        # dump  -> to a file

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)                 # load  <- from a file

# (dumps / loads - with an "s" - work with strings instead of files)
```

| JSON | Python |
|------|--------|
| object | `dict` |
| array | `list` |
| string | `str` |
| number | `int` / `float` |
| `true` / `false` | `True` / `False` |
| `null` | `None` |

## Console input/output

```python
name = input("Name? ")      # read a line from the keyboard (always a str)
print("hi", name)

import sys
print("error!", file=sys.stderr)   # write to stderr
```

---

## Gotchas for C#/TS developers

1. Always pass `encoding="utf-8"` (Windows' default encoding isn't UTF-8 for files).
2. `"w"` mode **wipes the file** the moment it opens.
3. `f.write()` doesn't add newlines, and lines you read **do** include `"\n"`. Use `.rstrip("\n")`
   or `.splitlines()`.
4. CSV values are always strings. Convert with `int()`/`float()`.
5. Relative paths are relative to the **current working directory**, not the script's location.
   Use `Path(__file__).parent` when that matters.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
The checks create files in a temporary folder, so nothing is left behind.
