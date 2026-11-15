"""
10 - Pythonic idioms: examples
Run me:  python examples.py
"""
import functools
import time
from contextlib import contextmanager

numbers = [5, -3, 8, 0, -1, 12, 7]
words = ["python", "is", "really", "fun"]

# --- List comprehensions --------------------------------------------------------------
print("--- List comprehensions ---")

# The loop way...
doubled_loop = []
for n in numbers:
    doubled_loop.append(n * 2)

# ...and the comprehension way
doubled = [n * 2 for n in numbers]
print("doubled:", doubled, doubled == doubled_loop)

positives = [n for n in numbers if n > 0]
print("positives:", positives)

squares_of_positives = [n * n for n in numbers if n > 0]
print("squares of positives:", squares_of_positives)

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print("labels:", labels)

grid = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in grid for value in row]      # read it like nested for loops
print("flattened:", flat)

# --- Dict & set comprehensions --------------------------------------------------------------
print("\n--- Dict & set comprehensions ---")
lengths = {word: len(word) for word in words}
print("lengths:", lengths)
print("unique lengths:", {len(word) for word in words})
prices = {"apple": 1.0, "melon": 3.5, "kiwi": 0.75}
expensive = {name: price for name, price in prices.items() if price > 0.9}
print("expensive:", expensive)

# --- any / all / sum / min / max with generator expressions -----------------------------------
print("\n--- any / all ---")
print("any negative?", any(n < 0 for n in numbers))
print("all under 100?", all(n < 100 for n in numbers))
print("sum of squares:", sum(n * n for n in numbers))
print("longest word:", max(words, key=len))
print("first > 6:", next(n for n in numbers if n > 6))
print("first > 99 (with default):", next((n for n in numbers if n > 99), None))


# --- Generators -----------------------------------------------------------------------------------
def countdown(n):
    print("  (countdown started)")
    while n > 0:
        yield n
        n -= 1
    print("  (countdown finished)")


print("\n--- Generators ---")
gen = countdown(3)
print("generator created, nothing has run yet:", gen)
for value in gen:
    print("got", value)
print("second loop over the same generator:", list(gen), "<- it's exhausted")


def fibonacci():
    """An INFINITE generator - fine, because it's lazy."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


first_ten = []
for number in fibonacci():
    if len(first_ten) == 10:
        break
    first_ten.append(number)
print("first ten fibonacci:", first_ten)

big_sum = sum(n for n in range(1_000_000))   # no million-item list is ever built
print("sum of 0..999999:", big_sum)

# --- Unpacking --------------------------------------------------------------------------------------
print("\n--- Unpacking ---")
first, *rest = numbers
print("first:", first, "rest:", rest)
*start, last = numbers
print("start:", start, "last:", last)

defaults = {"theme": "light", "font": 12}
overrides = {"theme": "dark"}
print("merged:", {**defaults, **overrides})
print("merged with |:", defaults | overrides)
print("combined lists:", [*words, *["!"]])

for index, (word, size) in enumerate(lengths.items()):
    print(index, word, size)

# Walrus
print("\n--- Walrus := ---")
data = [3, 8, 1]
if (count := len(data)) > 2:
    print(f"list is long ({count} items)")


# --- Decorators -------------------------------------------------------------------------------------
def logged(func):
    @functools.wraps(func)          # keeps func's name/docstring on the wrapper
    def wrapper(*args, **kwargs):
        print(f"  -> calling {func.__name__}{args}")
        result = func(*args, **kwargs)
        print(f"  <- {func.__name__} returned {result!r}")
        return result
    return wrapper


def repeat(times):
    """A decorator FACTORY: takes arguments and returns a decorator."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


@logged
def add(a, b):
    return a + b


@repeat(3)
def roll():
    return "rolled!"


print("\n--- Decorators ---")
add(2, 3)
print("name preserved by functools.wraps:", add.__name__)
print(roll())


# --- Context managers -----------------------------------------------------------------------------------
@contextmanager
def timer(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"  {label} took {elapsed * 1000:.1f} ms")


@contextmanager
def announce(name):
    print(f"  entering {name}")
    try:
        yield name.upper()          # the value after `as`
    finally:
        print(f"  leaving {name} (always runs)")


print("\n--- Context managers ---")
with timer("summing"):
    sum(range(200_000))

with announce("block") as shouted:
    print("  inside, got:", shouted)

try:
    with announce("risky block"):
        raise ValueError("oops")
except ValueError:
    print("  the exception still propagated, but cleanup ran first")
