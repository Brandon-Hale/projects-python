"""
06 - Classes: exercises

Fill in each class. Delete every `raise NotImplementedError` line you
replace, then run:  python exercises.py
"""
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Exercise 1: Counter
# A counter that starts at 0.
#   c = Counter()
#   c.increment(); c.increment()
#   c.value        ->  2
#   c.reset()
#   c.value        ->  0
# ---------------------------------------------------------------------------
class Counter:
    def __init__(self):
        raise NotImplementedError  # create self.value here

    def increment(self):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 2: Rectangle
# Store width and height. Add area() and perimeter() methods, and a
# __str__ that returns e.g. "Rectangle(3x4)".
#   r = Rectangle(3, 4)
#   r.area()       ->  12
#   r.perimeter()  ->  14
#   str(r)         ->  "Rectangle(3x4)"
# ---------------------------------------------------------------------------
class Rectangle:
    def __init__(self, width, height):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 3: Bank account
# Start with a balance (default 0).
#   deposit(amount)  - adds to the balance
#   withdraw(amount) - if there's enough money, subtract it and return True;
#                      otherwise leave the balance alone and return False
#   acct = BankAccount(100)
#   acct.withdraw(30)   ->  True   (balance now 70)
#   acct.withdraw(500)  ->  False  (balance still 70)
# ---------------------------------------------------------------------------
class BankAccount:
    def __init__(self, balance=0):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 4: Temperature with a property
# Store celsius. Add a READ-ONLY property `fahrenheit` (F = C * 9 / 5 + 32).
#   t = Temperature(100)
#   t.fahrenheit   ->  212.0       (note: no brackets - it's a property)
# ---------------------------------------------------------------------------
class Temperature:
    def __init__(self, celsius):
        raise NotImplementedError

    # add a @property called fahrenheit here


# ---------------------------------------------------------------------------
# Exercise 5: Inheritance
# Animal is done for you. Create Dog and Cat SUBCLASSES of Animal that
# override speak() to return "Woof" and "Meow".
#   Dog("Rex").describe()  ->  "Rex says Woof"
#   Cat("Tom").describe()  ->  "Tom says Meow"
# ---------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.name} says {self.speak()}"


# Write class Dog(Animal) and class Cat(Animal) here.


# ---------------------------------------------------------------------------
# Exercise 6: Dataclass
# Point is a dataclass (that gives you __init__, __repr__ and == for free).
# Add a distance_to(other) method returning the straight-line distance.
# Hint: ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#   Point(0, 0).distance_to(Point(3, 4))  ->  5.0
# ---------------------------------------------------------------------------
@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other):
        raise NotImplementedError


# ---------------------------------------------------------------------------
# Exercise 7: Stack
# A last-in-first-out stack backed by a list.
#   push(item)   - add to the top
#   pop()        - remove and return the top item
#   peek()       - return the top item WITHOUT removing it
#   is_empty()   - True if there's nothing in it
#   len(stack)   - number of items (implement __len__)
# ---------------------------------------------------------------------------
class Stack:
    def __init__(self):
        raise NotImplementedError

    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError


# =============================================================================
# CHECKS - run this file with:  python exercises.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
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


@check
def ex01_counter():
    c = Counter()
    expect(c.value, 0, "A new Counter's value")
    c.increment()
    c.increment()
    expect(c.value, 2, "value after two increments")
    c.reset()
    expect(c.value, 0, "value after reset()")


@check
def ex02_rectangle():
    r = Rectangle(3, 4)
    expect(r.area(), 12, "Rectangle(3, 4).area()")
    expect(r.perimeter(), 14, "Rectangle(3, 4).perimeter()")
    expect(str(r), "Rectangle(3x4)", "str(Rectangle(3, 4))")


@check
def ex03_bank_account():
    acct = BankAccount(100)
    expect(acct.balance, 100, "BankAccount(100).balance")
    expect(acct.withdraw(30), True, "withdraw(30)")
    expect(acct.balance, 70, "balance after withdrawing 30")
    expect(acct.withdraw(500), False, "withdraw(500)")
    expect(acct.balance, 70, "balance after a failed withdrawal")
    acct.deposit(5)
    expect(acct.balance, 75, "balance after deposit(5)")
    expect(BankAccount().balance, 0, "BankAccount().balance")


@check
def ex04_temperature():
    t = Temperature(100)
    assert isinstance(type(t).__dict__.get("fahrenheit"), property), \
        "fahrenheit should be a @property"
    expect(t.fahrenheit, 212.0, "Temperature(100).fahrenheit")
    t.celsius = 0
    expect(t.fahrenheit, 32.0, "fahrenheit after setting celsius to 0")


@check
def ex05_inheritance():
    if "Dog" not in globals() or "Cat" not in globals():
        raise NotImplementedError
    assert issubclass(Dog, Animal), "Dog should inherit from Animal"
    assert issubclass(Cat, Animal), "Cat should inherit from Animal"
    expect(Dog("Rex").describe(), "Rex says Woof", 'Dog("Rex").describe()')
    expect(Cat("Tom").describe(), "Tom says Meow", 'Cat("Tom").describe()')


@check
def ex06_point():
    expect(Point(0, 0).distance_to(Point(3, 4)), 5.0, "Point(0, 0).distance_to(Point(3, 4))")
    expect(Point(1, 1).distance_to(Point(1, 1)), 0.0, "Point(1, 1).distance_to(Point(1, 1))")


@check
def ex07_stack():
    s = Stack()
    expect(s.is_empty(), True, "A new stack's is_empty()")
    s.push(1)
    s.push(2)
    s.push(3)
    expect(len(s), 3, "len(stack) after three pushes")
    expect(s.peek(), 3, "peek()")
    expect(len(s), 3, "len(stack) after peek() (peek shouldn't remove)")
    expect(s.pop(), 3, "first pop()")
    expect(s.pop(), 2, "second pop()")
    expect(s.is_empty(), False, "is_empty() with one item left")


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
