"""
12 - Testing: exercises

This time YOU write the tests.

Each exercise is a test function that receives the function to test as a
parameter (so the checker can hand it different versions). Use `assert` to
check that the function behaves correctly.

The checker runs your test:
  - against a CORRECT implementation -> your test must PASS
  - against several BUGGY ones       -> your test must FAIL (catch the bug!)

So think about edge cases: empty input, zero, negatives, one item...

Delete each `raise NotImplementedError` line, write your asserts,
then run:  python exercises.py
"""


# ---------------------------------------------------------------------------
# Exercise 1: Test add
# `add(a, b)` should return a + b.
# Example assert:   assert add(2, 3) == 5
# (One assert might not catch every bug - think about what could go wrong!)
# ---------------------------------------------------------------------------
def test_add(add):
    raise NotImplementedError  # delete this line and write your asserts


# ---------------------------------------------------------------------------
# Exercise 2: Test is_even
# `is_even(n)` should return True for even numbers and False for odd ones.
# Make sure you test both outcomes!
# ---------------------------------------------------------------------------
def test_is_even(is_even):
    raise NotImplementedError  # delete this line and write your asserts


# ---------------------------------------------------------------------------
# Exercise 3: Test reverse
# `reverse(text)` should return the string backwards: "abc" -> "cba".
# ---------------------------------------------------------------------------
def test_reverse(reverse):
    raise NotImplementedError  # delete this line and write your asserts


# ---------------------------------------------------------------------------
# Exercise 4: Test find_max
# `find_max(numbers)` should return the largest number in a non-empty list.
# Hint: what if the biggest number is first? last? What if they're all negative?
# ---------------------------------------------------------------------------
def test_find_max(find_max):
    raise NotImplementedError  # delete this line and write your asserts


# ---------------------------------------------------------------------------
# Exercise 5: Test that an error is raised
# `safe_sqrt(x)` should return the square root of x, and RAISE ValueError
# if x is negative.
# Test both! For the error, use try / except / else:
#
#   try:
#       safe_sqrt(-1)
#   except ValueError:
#       pass                      # good - that's what we wanted
#   else:
#       raise AssertionError("safe_sqrt(-1) should raise ValueError")
#
# (In pytest you'd write:  with pytest.raises(ValueError): safe_sqrt(-1) )
# ---------------------------------------------------------------------------
def test_safe_sqrt(safe_sqrt):
    raise NotImplementedError  # delete this line and write your asserts


# ---------------------------------------------------------------------------
# Exercise 6: Test a class
# `make_stack()` returns a NEW empty stack with push(item), pop() and
# is_empty(). pop() returns the most recently pushed item (last in, first out).
# ---------------------------------------------------------------------------
def test_stack(make_stack):
    raise NotImplementedError  # delete this line and write your asserts


# =============================================================================
# CHECKS - run this file with:  python exercises.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
import math
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


def judge(your_test, correct, buggy_versions):
    """Your test must pass on `correct` and fail on every buggy version."""
    try:
        your_test(correct)
    except NotImplementedError:
        raise
    except AssertionError as error:
        raise AssertionError(f"your test FAILED on the CORRECT implementation ({error})")
    for description, buggy in buggy_versions:
        try:
            your_test(buggy)
        except NotImplementedError:
            raise
        except Exception:
            continue  # good - the bug was caught
        raise AssertionError(f"your test didn't catch this bug: {description}")


@check
def ex01_test_add():
    judge(test_add, lambda a, b: a + b, [
        ("it subtracts instead of adding", lambda a, b: a - b),
        ("it multiplies instead of adding", lambda a, b: a * b),
        ("it always returns 5", lambda a, b: 5),
        ("it ignores b", lambda a, b: a),
    ])


@check
def ex02_test_is_even():
    judge(test_is_even, lambda n: n % 2 == 0, [
        ("it always returns True", lambda n: True),
        ("it always returns False", lambda n: False),
        ("it's backwards (checks for odd)", lambda n: n % 2 == 1),
    ])


@check
def ex03_test_reverse():
    judge(test_reverse, lambda text: text[::-1], [
        ("it returns the text unchanged", lambda text: text),
        ("it drops the first character", lambda text: text[::-1][:-1]),
        ("it only swaps the first and last characters",
         lambda text: text if len(text) < 2 else text[-1] + text[1:-1] + text[0]),
    ])


@check
def ex04_test_find_max():
    def starts_at_zero(numbers):
        best = 0
        for n in numbers:
            if n > best:
                best = n
        return best

    def skips_last(numbers):
        return max(numbers[:-1]) if len(numbers) > 1 else numbers[0]

    judge(test_find_max, max, [
        ("it returns the first item", lambda numbers: numbers[0]),
        ("it returns the minimum", min),
        ("it starts from 0, so it's wrong when every number is negative", starts_at_zero),
        ("it never looks at the last item", skips_last),
    ])


@check
def ex05_test_safe_sqrt():
    def correct(x):
        if x < 0:
            raise ValueError("negative")
        return math.sqrt(x)

    def returns_zero(x):
        return 0.0 if x < 0 else math.sqrt(x)

    def wrong_error(x):
        if x < 0:
            raise TypeError("negative")
        return math.sqrt(x)

    def raises_for_zero(x):
        if x <= 0:
            raise ValueError("not positive")
        return math.sqrt(x)

    judge(test_safe_sqrt, correct, [
        ("it returns 0.0 for negatives instead of raising", returns_zero),
        ("it raises TypeError instead of ValueError", wrong_error),
        ("it halves instead of square-rooting", lambda x: correct(x) and x / 2),
        ("it raises for 0, which is a valid input", raises_for_zero),
    ])


@check
def ex06_test_stack():
    class GoodStack:
        def __init__(self):
            self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def is_empty(self):
            return not self.items

    class FifoStack(GoodStack):
        def pop(self):
            return self.items.pop(0)

    class NeverEmpty(GoodStack):
        def is_empty(self):
            return False

    class AlwaysEmpty(GoodStack):
        def is_empty(self):
            return True

    class PeekingPop(GoodStack):
        def pop(self):
            return self.items[-1]

    judge(test_stack, GoodStack, [
        ("pop() returns the OLDEST item (it's a queue, not a stack)", FifoStack),
        ("is_empty() always returns False", NeverEmpty),
        ("is_empty() always returns True", AlwaysEmpty),
        ("pop() doesn't actually remove the item", PeekingPop),
    ])


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
