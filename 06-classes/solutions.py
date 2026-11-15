"""
06 - Classes: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""
from dataclasses import dataclass


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

    def describe(self):
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


# =============================================================================
# CHECKS - run this file with:  python solutions.py
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
