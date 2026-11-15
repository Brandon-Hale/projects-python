# 12 · Testing

Writing tests in Python: `assert`, the built-in `unittest`, and the community standard, **pytest**.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)
· [`calculator.py`](calculator.py) (code under test) · [`test_calculator.py`](test_calculator.py) (pytest tests)

---

## assert

The simplest test is an `assert` statement:

```python
assert add(2, 2) == 4
assert add(2, 2) == 4, "addition is broken"     # optional message
```

If the condition is false, it raises `AssertionError`. You've been relying on this all course:
every exercises check uses `assert`!

## pytest: the standard choice

[pytest](https://docs.pytest.org/) is what most Python projects use. It's like **xUnit/NUnit**
for C# or **Jest/Vitest** for TS, but with less ceremony:

- Tests are plain functions whose names start with `test_`.
- They live in files named `test_*.py` (or `*_test.py`).
- You use plain `assert`. There's no `Assert.Equal`/`expect().toBe()`, because pytest rewrites
  `assert` to show detailed failure messages.

```python
# test_calculator.py
from calculator import add

def test_add_two_positives():
    assert add(2, 3) == 5
```

```bash
pip install pytest        # inside a venv (module 08)
pytest                    # finds and runs every test in this folder and below
pytest -v                 # verbose: one line per test
pytest -k add             # only tests with "add" in the name
pytest test_calculator.py::test_add_two_positives   # one specific test
```

### Testing exceptions

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):     # C#: Assert.Throws<...>
        divide(1, 0)

    with pytest.raises(ValueError, match="negative"):   # also check the message
        sqrt(-1)
```

### Parametrised tests: one test, many inputs

```python
@pytest.mark.parametrize("a, b, expected", [     # xUnit [Theory] + [InlineData]
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

### Fixtures: shared setup

```python
@pytest.fixture
def account():                      # setup code
    return BankAccount(balance=100)

def test_withdraw(account):         # pytest passes the fixture in by NAME
    account.withdraw(30)
    assert account.balance == 70
```

Fixtures replace the constructor/`[SetUp]`/`beforeEach` pattern. pytest also ships with
built-in fixtures, such as `tmp_path` (a fresh temporary folder) and `capsys` (captures printed output).

### Floats

```python
assert 0.1 + 0.2 == pytest.approx(0.3)
```

## unittest: built in, class-based

Python also ships with `unittest`, which is modelled on JUnit/NUnit. You'll see it in older code:

```python
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

if __name__ == "__main__":
    unittest.main()
```

pytest can run `unittest` tests too, so you can mix them.

## What makes a good test?

1. **Test behaviour, not implementation.** Check what goes in and what comes out.
2. **Cover the edges.** Try empty input, zero, negatives, one item, duplicates, and the boundary values.
3. **One reason to fail.** Small focused tests tell you *what* broke.
4. **Make it fail first.** If a test can't fail, it isn't testing anything. (The exercises below
   are built around this idea.)

---

## Gotchas for C#/TS developers

1. Test files and functions **must** start with `test_`, or pytest won't find them.
2. Don't name a file `pytest.py` or `test.py`; it will shadow the real modules.
3. Run `pytest` from the folder containing the tests (or the project root) so imports resolve.

## Your turn

These exercises flip things around: **you write the tests**. Each check runs your test against
a **correct** implementation (your test must pass) and some **buggy** ones (your test must
catch every bug). Open [`exercises.py`](exercises.py) and run `python exercises.py`.

Then, as a bonus, install pytest and run `pytest -v` in this folder.
