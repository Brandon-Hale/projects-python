# 08 · Modules and packages

Splitting code across files, importing, a tour of the standard library, and installing
third-party packages with `pip` and virtual environments.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)
· [`string_tools.py`](string_tools.py) (a module) · [`shapes/`](shapes/) (a package)

---

## Modules = files

Every `.py` file is a **module**. Its file name is the module name.
[`string_tools.py`](string_tools.py) in this folder is the module `string_tools`.

```python
import string_tools                      # import the whole module
string_tools.slugify("Hello World")

from string_tools import slugify         # import one name
slugify("Hello World")

from string_tools import slugify as slug # rename on import
import string_tools as st                # alias the module

from string_tools import *               # imports everything: avoid it, it hides where names come from
```

> **C#:** a module is roughly a static class plus a namespace. **TS:** it's exactly an ES module,
> except that everything top-level is "exported" automatically. A leading `_` marks a name as private by convention.

## Packages = folders

A **package** is a folder of modules, usually with an `__init__.py` file:

```
shapes/
    __init__.py     # runs when the package is imported; can be empty
    circle.py
    square.py
```

```python
from shapes import circle          # import a module from the package
from shapes.circle import area     # import a name from a module in the package
import shapes                      # gets whatever __init__.py exposes
```

## `if __name__ == "__main__":`

When Python runs a file directly, that file's `__name__` is `"__main__"`. When the file is
*imported*, `__name__` is the module's name. So:

```python
def main():
    ...

if __name__ == "__main__":     # only runs when you do `python this_file.py`
    main()
```

This lets a file be both an importable module and a runnable script. It's the closest thing
Python has to `static void Main()`. Every `exercises.py` in this course uses it.

## How Python finds modules

When you `import x`, Python searches:
1. the folder of the script you ran
2. the installed standard library
3. installed third-party packages (`site-packages`)

So run scripts **from their folder** (or by path). Never name your own file the same as a
standard library module (`random.py`, `json.py`, `math.py`), because it will shadow the real one!

## The standard library: "batteries included"

You get a lot without installing anything:

| Module | Use it for | C#/.NET equivalent |
|--------|-----------|--------------------|
| `math` | `sqrt`, `pi`, `floor`, `ceil` | `System.Math` |
| `random` | random numbers, `choice`, `shuffle` | `System.Random` |
| `datetime` | dates, times, durations | `DateTime`, `TimeSpan` |
| `collections` | `Counter`, `defaultdict`, `deque`, `namedtuple` | assorted generic collections |
| `itertools` | combinations, permutations, chaining iterables | LINQ extras |
| `pathlib` | file paths | `System.IO.Path` |
| `json` | JSON encode/decode | `System.Text.Json` |
| `os`, `sys` | environment, arguments, process info | `Environment` |
| `re` | regular expressions | `Regex` |
| `time` | sleeping, timing | `Thread.Sleep`, `Stopwatch` |
| `logging` | logging | `ILogger` |
| `argparse` | command-line arguments | System.CommandLine |

Browse them all at <https://docs.python.org/3/library/>.

## Third-party packages: pip and virtual environments

`pip` is Python's NuGet/npm. Packages come from [PyPI](https://pypi.org/).

**Always use a virtual environment** (venv) per project. It's like a local `node_modules`, so
projects don't fight over package versions:

```bash
# create one (once per project)
python -m venv .venv

# activate it (every new terminal)
.venv\Scripts\activate          # Windows (PowerShell / cmd)
source .venv/bin/activate       # macOS / Linux / Git Bash

# install packages into it
pip install requests

# record what you installed (like package.json / .csproj references)
pip freeze > requirements.txt

# reinstall everything elsewhere
pip install -r requirements.txt

# leave the venv
deactivate
```

> Newer projects often use a `pyproject.toml` file plus tools like **uv** or **poetry**. These are
> faster, more modern equivalents of the commands above. Learn plain `venv` + `pip` first, because
> everything else builds on them.

---

## Gotchas for C#/TS developers

1. Don't name your files after standard modules (`random.py`, `test.py`, `email.py`...).
2. Imports run code. Everything at the top level of the imported file executes on first import.
   Keep side effects under `if __name__ == "__main__":`.
3. A module is only executed once per process. Later imports reuse it.
4. Forgetting to activate the venv means `pip install` installs globally and your editor can't
   find packages. In VS Code, pick the `.venv` interpreter (Ctrl+Shift+P → "Python: Select Interpreter").

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
