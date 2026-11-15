"""
06 - Classes: examples
Run me:  python examples.py
"""
from dataclasses import dataclass, field


# --- A basic class ---------------------------------------------------------------
class Dog:
    species = "Canis familiaris"   # class attribute - shared by every Dog

    def __init__(self, name, age):
        self.name = name           # instance attributes
        self.age = age

    def bark(self):
        return f"{self.name} says woof"

    def birthday(self):
        self.age += 1


print("--- Basic class ---")
rex = Dog("Rex", 3)
fido = Dog("Fido", 5)
print(rex.bark())
rex.birthday()
print(rex.name, "is now", rex.age)
print("species via instance:", rex.species, "| via class:", Dog.species)

# Attributes can even be added on the fly (possible, but avoid it!)
fido.favourite_toy = "ball"
print(fido.favourite_toy)

# Without __str__, printing an object isn't very useful:
print(rex)


# --- __str__, __repr__, __eq__ ---------------------------------------------------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):                  # for humans: print(book)
        return f"'{self.title}' by {self.author}"

    def __repr__(self):                 # for developers: repr(book), the REPL, lists
        return f"Book({self.title!r}, {self.author!r})"

    def __eq__(self, other):            # define what == means
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author


print("\n--- Dunder methods ---")
book = Book("Dune", "Frank Herbert")
print(book)                     # uses __str__
print(repr(book))               # uses __repr__
print([book])                   # lists show the __repr__ of their items
print(book == Book("Dune", "Frank Herbert"))   # True thanks to __eq__
print(book is Book("Dune", "Frank Herbert"))   # False - different objects


# --- Properties ----------------------------------------------------------------------------
class Circle:
    def __init__(self, radius):
        self.radius = radius        # goes through the setter below!

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius must be >= 0")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2


print("\n--- Properties ---")
c = Circle(2)
print("radius:", c.radius, "area:", c.area)   # no () - properties look like fields
c.radius = 3
print("radius:", c.radius, "area:", round(c.area, 2))
try:
    c.radius = -1
except ValueError as error:
    print("setter rejected it:", error)


# --- Inheritance -------------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name)
        self.indoor = indoor

    def speak(self):
        return "Meow"


class Cow(Animal):
    def speak(self):
        return "Moo"


print("\n--- Inheritance ---")
for animal in [Animal("Generic"), Cat("Tom"), Cow("Daisy")]:
    print(animal.describe())

tom = Cat("Tom")
print("isinstance(tom, Animal):", isinstance(tom, Animal))
print("issubclass(Cat, Animal):", issubclass(Cat, Animal))


# --- classmethod & staticmethod ------------------------------------------------------------------
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        return cls((fahrenheit - 32) * 5 / 9)

    @staticmethod
    def is_valid(celsius):
        return celsius >= -273.15

    def __repr__(self):
        return f"Temperature({self.celsius:.1f}C)"


print("\n--- classmethod / staticmethod ---")
print(Temperature(25))
print(Temperature.from_fahrenheit(212))
print(Temperature.is_valid(-300))


# --- Making a class work with len(), in, and for -----------------------------------------------------
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __contains__(self, song):
        return song in self._songs

    def __iter__(self):
        return iter(self._songs)


print("\n--- Container protocol ---")
playlist = Playlist("Road trip")
playlist.add("Song A")
playlist.add("Song B")
print("len:", len(playlist))
print("'Song A' in playlist:", "Song A" in playlist)
for song in playlist:
    print(" -", song)


# --- Dataclasses -----------------------------------------------------------------------------------------
@dataclass
class Point:
    x: float
    y: float = 0.0

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass(frozen=True)
class Money:
    amount: int
    currency: str = "AUD"


@dataclass
class ShoppingCart:
    owner: str
    items: list = field(default_factory=list)   # the safe way to default to a list


print("\n--- Dataclasses ---")
p = Point(3, 4)
print(p)
print("distance:", p.distance_from_origin())
print("equal by value:", Point(1, 2) == Point(1, 2))
m = Money(100)
print(m)
try:
    m.amount = 5
except Exception as error:
    print("frozen dataclass:", type(error).__name__)
cart = ShoppingCart("ada")
cart.items.append("book")
print(cart)
