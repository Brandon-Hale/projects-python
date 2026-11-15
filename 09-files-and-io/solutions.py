"""
09 - Files and I/O: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""
import csv
import json
from pathlib import Path


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()


def count_non_blank_lines(path):
    count = 0
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():        # strip() leaves "" for blank lines, which is falsy
                count += 1
    return count


def append_line(path, line):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def csv_totals(path):
    totals = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["name"]
            totals[name] = totals.get(name, 0) + float(row["amount"])
    return totals


def python_files_in(folder):
    return sorted(p.name for p in Path(folder).glob("*.py"))


def read_or_default(path, default=""):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return default


# =============================================================================
# CHECKS - run this file with:  python solutions.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
import tempfile
from contextlib import redirect_stdout

_checks = []


def check(test):
    _checks.append(test)
    return test


def output_of(func, *args):
    """Run func and return everything it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args)
    return buffer.getvalue()


def expect(actual, expected, label):
    assert actual == expected, f"{label} should be {expected!r}, got {actual!r}"


def in_temp_folder(test):
    """Run the test with a fresh, empty temporary folder that's deleted afterwards."""
    def wrapper():
        with tempfile.TemporaryDirectory() as tmp:
            test(Path(tmp))
    wrapper.__name__ = test.__name__
    return wrapper


def put(path, text):
    path.write_text(text, encoding="utf-8", newline="")


def contents(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


@check
@in_temp_folder
def ex01_write_lines(tmp):
    path = tmp / "out.txt"
    put(path, "old content that should be replaced\n")
    write_lines(path, ["a", "b"])
    expect(contents(path), "a\nb\n", "the file's contents")


@check
@in_temp_folder
def ex02_read_lines(tmp):
    path = tmp / "in.txt"
    put(path, "a\nb\n")
    expect(read_lines(path), ["a", "b"], 'read_lines of "a\\nb\\n"')


@check
@in_temp_folder
def ex03_count_non_blank_lines(tmp):
    path = tmp / "in.txt"
    put(path, "a\n\n  \nb\n")
    expect(count_non_blank_lines(path), 2, 'count_non_blank_lines of "a\\n\\n  \\nb\\n"')


@check
@in_temp_folder
def ex04_append_line(tmp):
    path = tmp / "log.txt"
    append_line(path, "first")
    expect(contents(path), "first\n", "the file after appending to a missing file")
    append_line(path, "second")
    expect(contents(path), "first\nsecond\n", "the file after a second append")


@check
@in_temp_folder
def ex05_save_json(tmp):
    path = tmp / "data.json"
    data = {"name": "Ada", "skills": ["maths", "code"], "active": True}
    save_json(path, data)
    expect(json.loads(contents(path)), data, "the JSON in the file")


@check
@in_temp_folder
def ex06_load_json(tmp):
    path = tmp / "data.json"
    put(path, '{"name": "Alan", "scores": [1, 2], "ok": false}')
    expect(load_json(path), {"name": "Alan", "scores": [1, 2], "ok": False}, "load_json(...)")


@check
@in_temp_folder
def ex07_csv_totals(tmp):
    path = tmp / "money.csv"
    put(path, "name,amount\nada,10\nalan,5.5\nada,2.5\n")
    expect(csv_totals(path), {"ada": 12.5, "alan": 5.5}, "csv_totals(...)")


@check
@in_temp_folder
def ex08_python_files_in(tmp):
    for name in ["b.py", "a.py", "notes.txt", "c.pyc"]:
        put(tmp / name, "")
    (tmp / "sub").mkdir()
    put(tmp / "sub" / "deep.py", "")
    expect(python_files_in(tmp), ["a.py", "b.py"], "python_files_in(folder)")


@check
@in_temp_folder
def ex09_read_or_default(tmp):
    path = tmp / "exists.txt"
    put(path, "hello")
    expect(read_or_default(path), "hello", "read_or_default(existing file)")
    expect(read_or_default(tmp / "nope.txt", "n/a"), "n/a", 'read_or_default(missing file, "n/a")')


if __name__ == "__main__":
    passed = 0
    for test in _checks:
        try:
            test()
        except NotImplementedError:
            print(f"[TODO]  {test.__name__}")
        except AssertionError as error:
            print(f"[FAIL]  {test.__name__}: {error}")
        except Exception as error:
            print(f"[ERROR] {test.__name__}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"[PASS]  {test.__name__}")
    print(f"\n{passed}/{len(_checks)} exercises passing")
