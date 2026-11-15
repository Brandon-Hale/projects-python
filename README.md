# Learn Python (for people who already code)

A hands-on Python course, organised as numbered folders you work through in order.
Each folder covers one area of the language with **explanations**, **runnable examples**,
and **exercises you write yourself** — with built-in checks so you know when you've got it right.

It's written with C# and TypeScript developers in mind, so most topics include a
"here's how you'd do it in C#/TS" comparison. If you're brand new to programming you can
still follow along — just skim past the comparisons.

---

## Course map

| #  | Module | What you'll learn |
|----|--------|-------------------|
| 01 | [Basics](01-basics/) | Variables, types, numbers, `print`, f-strings, `None`, type conversion |
| 02 | [Control flow](02-control-flow/) | `if`/`elif`/`else`, truthiness, `for`, `while`, `range`, `break`/`continue`, `match` |
| 03 | [Functions](03-functions/) | `def`, default & keyword args, `*args`/`**kwargs`, closures, lambdas |
| 04 | [Collections](04-collections/) | `list`, `tuple`, `dict`, `set`, slicing, `enumerate`, `zip` |
| 05 | [Strings](05-strings/) | String methods, slicing, formatting, `split`/`join` |
| 06 | [Classes](06-classes/) | Classes, `self`, properties, inheritance, dunder methods, dataclasses |
| 07 | [Errors](07-errors/) | `try`/`except`/`else`/`finally`, raising, custom exceptions |
| 08 | [Modules & packages](08-modules-and-packages/) | `import`, your own modules, the standard library, `pip` & virtual environments |
| 09 | [Files & I/O](09-files-and-io/) | Reading/writing files, `with`, `pathlib`, CSV, JSON |
| 10 | [Pythonic idioms](10-pythonic-idioms/) | Comprehensions, generators, `any`/`all`, decorators, context managers |
| 11 | [Type hints](11-type-hints/) | Annotations, generics, `Optional`, `Protocol`, running a type checker |
| 12 | [Testing](12-testing/) | `assert`, writing good tests, `pytest` |

---

## Setup

1. **Install Python 3.10 or newer** from [python.org](https://www.python.org/downloads/).
   On Windows, tick **"Add python.exe to PATH"** during install.
2. Check it works:
   ```bash
   python --version      # Windows (or: py --version)
   python3 --version     # macOS / Linux
   ```
3. **Clone this repo** (or fork it first so you can push your own answers):
   ```bash
   git clone <this-repo-url>
   cd <repo-folder>
   ```
4. **Recommended editor:** [VS Code](https://code.visualstudio.com/) with the official
   **Python** extension (by Microsoft). It gives you autocomplete, a debugger and a "Run" button.

> On macOS/Linux, use `python3` wherever this course says `python`.

---

## How each module works

Every folder has the same four files:

| File | What to do with it |
|------|--------------------|
| `README.md` | **Read first.** Explains the concepts with short code snippets and C#/TS comparisons. |
| `examples.py` | **Run it and read it.** Every line is commented. Change things and re-run to see what happens. |
| `exercises.py` | **Your work.** Small tasks like "write a loop that prints every even number up to 20". |
| `solutions.py` | **Only when stuck** — or to compare once you've passed. |

### Doing the exercises

Each exercise is a function with a description above it and a placeholder body:

```python
# Exercise 1: Greeting
# Return the string "Hello, <name>!" using an f-string.
#   greeting("Ada")  ->  "Hello, Ada!"
def greeting(name):
    raise NotImplementedError  # delete this line and write your code
```

Delete the `raise NotImplementedError` line, write your code, then run the file:

```bash
cd 01-basics
python exercises.py
```

You'll get a report like this:

```
[PASS]  ex01_greeting
[FAIL]  ex02_average: average(1, 2, 3) should be 2.0, got 6
[TODO]  ex03_minutes_to_hours
...
2/9 exercises passing
```

- **PASS** — nice, move on.
- **FAIL** — your code ran but gave the wrong answer. The message tells you what was expected.
- **TODO** — you haven't started this one yet.
- **ERROR** — your code crashed. The error type and message help you find out why.

Keep going until everything passes, then move to the next module.

> The checking code lives at the bottom of each `exercises.py`, below a big "CHECKS" banner.
> You don't need to understand it to start — by module 10 you'll be able to read all of it.

---

## C# / TypeScript → Python cheat sheet

| Concept | C# | TypeScript | Python |
|---------|----|-----------|--------|
| Variable | `var x = 5;` | `let x = 5;` | `x = 5` |
| Constant | `const int X = 5;` | `const x = 5;` | `X = 5` *(convention only)* |
| Null | `null` | `null` / `undefined` | `None` |
| Booleans | `true` / `false` | `true` / `false` | `True` / `False` |
| Logic | `&&` `\|\|` `!` | `&&` `\|\|` `!` | `and` `or` `not` |
| String interpolation | `$"Hi {name}"` | `` `Hi ${name}` `` | `f"Hi {name}"` |
| Block | `{ ... }` | `{ ... }` | `:` + indentation |
| Comment | `// ...` | `// ...` | `# ...` |
| If/else if | `else if` | `else if` | `elif` |
| For-each | `foreach (var x in xs)` | `for (const x of xs)` | `for x in xs:` |
| Counting loop | `for (int i = 0; i < 10; i++)` | `for (let i = 0; i < 10; i++)` | `for i in range(10):` |
| Increment | `i++` | `i++` | `i += 1` |
| Function | `int Add(int a, int b) { ... }` | `function add(a: number, b: number) { ... }` | `def add(a: int, b: int) -> int:` |
| Lambda | `x => x * 2` | `x => x * 2` | `lambda x: x * 2` |
| List | `List<int>` | `number[]` | `list[int]` |
| Dictionary | `Dictionary<string, int>` | `Record<string, number>` / `Map` | `dict[str, int]` |
| Length | `.Count` / `.Length` | `.length` | `len(x)` |
| Class constructor | `public Foo() { }` | `constructor() { }` | `def __init__(self):` |
| `this` | `this` | `this` | `self` *(explicit first parameter)* |
| Exceptions | `try / catch / finally` | `try / catch / finally` | `try / except / finally` |
| Imports | `using System.IO;` | `import fs from "fs";` | `import os` |
| Package manager | NuGet | npm | pip |

---

## Tips

- **Run things constantly.** Python has no compile step — edit, run, repeat.
- **Use the REPL.** Type `python` with no arguments to get an interactive prompt. Great for
  "what does this do?" questions. Exit with `exit()`.
- **`help()` and `dir()`** work on anything: `help(str.split)`, `dir([])`.
- **Read the errors from the bottom up.** The last line of a traceback says what went wrong;
  the lines above it say where.

## Contributing

Found a mistake or have an idea for a better exercise? Issues and pull requests are welcome.

## License

[MIT](LICENSE) — use it, share it, adapt it.
