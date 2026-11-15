# 06 · Classes

Defining classes, `self`, properties, inheritance, "dunder" methods, and dataclasses.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## A basic class

```python
class Dog:
    species = "Canis familiaris"          # class attribute (shared, like C# static)

    def __init__(self, name, age):        # the constructor
        self.name = name                  # instance attributes are created by assigning
        self.age = age

    def bark(self):                       # every method takes self first
        return f"{self.name} says woof"

rex = Dog("Rex", 3)                       # no `new` keyword
rex.bark()                                # "Rex says woof"
rex.name                                  # "Rex"
```

Key differences from C#/TS:

- **`self` is explicit.** It's the first parameter of every instance method (like `this`, but you
  write it yourself). When you call `rex.bark()`, Python passes `rex` as `self`.
- **Fields aren't declared up front.** You create them by assigning to `self.x` in `__init__`.
- **No `new`.** You call the class like a function.

## No access modifiers

Python has no `private`/`protected`/`public`. Naming conventions are used instead:

| Name | Meaning |
|------|---------|
| `name` | public |
| `_name` | "internal, please don't touch" (convention only) |
| `__name` | name-mangled to `_ClassName__name` to avoid clashes in subclasses (rarely needed) |

Python's philosophy is *"we're all consenting adults here."*

## Properties

Use `@property` to make a method behave like a field. This is C# get/set properties:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):                  # getter
        return self._radius

    @radius.setter
    def radius(self, value):           # setter (optional)
        if value < 0:
            raise ValueError("radius must be >= 0")
        self._radius = value

    @property
    def area(self):                    # computed, read-only
        return 3.14159 * self._radius ** 2

c = Circle(2)
c.area          # no () because it's a property
c.radius = 5    # calls the setter
```

> Start with plain attributes. Only switch to `@property` when you need logic. Callers won't
> notice the change, so no up-front `{ get; set; }` boilerplate is needed.

## Dunder ("magic") methods

Methods named `__like_this__` hook into Python's built-in behaviour:

| Method | Called by | C# equivalent |
|--------|-----------|---------------|
| `__init__(self, ...)` | `MyClass(...)` | constructor |
| `__str__(self)` | `str(obj)`, `print(obj)` | `ToString()` |
| `__repr__(self)` | `repr(obj)`, the REPL, debugger | `DebuggerDisplay` |
| `__eq__(self, other)` | `a == b` | `Equals()` / `operator ==` |
| `__lt__(self, other)` | `a < b`, `sorted()` | `IComparable` |
| `__len__(self)` | `len(obj)` | `.Count` |
| `__add__(self, other)` | `a + b` | `operator +` |
| `__contains__(self, x)` | `x in obj` | `.Contains()` |
| `__iter__(self)` | `for x in obj` | `IEnumerable` |

By default, `==` on objects compares **identity** (same object), just like reference types in C#.

## Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"

class Cat(Animal):                         # C#: class Cat : Animal
    def __init__(self, name, indoor):
        super().__init__(name)             # call the parent constructor
        self.indoor = indoor

    def speak(self):                       # override, no keyword needed
        return "Meow"

Cat("Tom", True).describe()                # "Tom says Meow"
```

- Every method is effectively **virtual**. There's no `virtual`/`override` keyword.
- `isinstance(tom, Animal)` is `True`.
- Multiple inheritance is allowed (`class C(A, B)`), but use it sparingly.

## Class methods and static methods

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):           # alternative constructor; gets the class as `cls`
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_valid(celsius):                 # just a function namespaced in the class
        return celsius >= -273.15

t = Temperature.from_fahrenheit(212)
```

## Dataclasses: Python's `record`

For classes that mostly hold data, `@dataclass` generates `__init__`, `__repr__`, and `__eq__`
for you:

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float = 0.0          # default value

p = Point(1, 2)
print(p)                    # Point(x=1, y=2)
p == Point(1, 2)            # True, compared by value

@dataclass(frozen=True)     # immutable, like a C# record / readonly struct
class Money:
    amount: int
    currency: str
```

> **C#:** `record Point(double X, double Y);`  **TS:** a class with a constructor shorthand.

---

## Gotchas for C#/TS developers

1. Forgetting `self` in a method definition gives you
   `TypeError: method() takes 0 positional arguments but 1 was given`.
2. Forgetting `self.` when reading an attribute gives you `NameError`.
3. Class attributes holding a **mutable** value (`items = []` at class level) are shared by
   **all instances**. Create them in `__init__` instead.
4. There's no method overloading. Use default arguments or `@classmethod` alternative constructors.
5. There are no interfaces. Python uses duck typing ("if it has a `.quack()` method, it's a duck").
   Module 11 shows `Protocol` for interface-like type checking.

## Your turn

Open [`exercises.py`](exercises.py), complete each class, and run `python exercises.py`.
