"""
03 - Functions: examples
Run me:  python examples.py
"""


# --- Basic function ------------------------------------------------------------
def greet(name):
    """Return a friendly greeting. (This is a docstring - try help(greet) in the REPL.)"""
    return f"Hello, {name}"


print("--- Basics ---")
print(greet("Ada"))


def no_return():
    x = 1 + 1   # does some work but never returns


print("no_return() gives:", no_return())  # None


# --- Defaults and keyword arguments ---------------------------------------------
def power(base, exponent=2):
    return base ** exponent


print("\n--- Defaults & keywords ---")
print(power(3))                  # 9  (exponent defaults to 2)
print(power(3, 3))               # 27
print(power(exponent=3, base=2)) # 8  (named, any order)


def connect(host, *, timeout=30, retries=3):
    """Everything after the bare * must be passed by name."""
    return f"connecting to {host} (timeout={timeout}, retries={retries})"


print(connect("example.com"))
print(connect("example.com", timeout=5))
# connect("example.com", 5)   # <- uncomment: TypeError, timeout is keyword-only


# --- *args and **kwargs -------------------------------------------------------------
def total(*numbers):
    print("  numbers is a", type(numbers).__name__, numbers)
    return sum(numbers)


def show(**options):
    print("  options is a", type(options).__name__, options)
    for key, value in options.items():
        print(f"  {key} = {value}")


print("\n--- *args / **kwargs ---")
print(total(1, 2, 3))
print(total())
show(colour="red", size=3)

# Spreading values INTO a call
nums = [10, 20, 30]
print(total(*nums))                    # same as total(10, 20, 30)
settings = {"timeout": 1, "retries": 9}
print(connect("db.local", **settings))  # same as connect("db.local", timeout=1, retries=9)


# --- Multiple return values ---------------------------------------------------------
def min_max(numbers):
    return min(numbers), max(numbers)


print("\n--- Multiple returns ---")
result = min_max([3, 1, 4, 1, 5])
print("as a tuple:", result)
low, high = min_max([3, 1, 4, 1, 5])
print("unpacked:", low, high)


# --- Functions are values ---------------------------------------------------------------
def shout(text):
    return text.upper() + "!"


def whisper(text):
    return text.lower() + "..."


def apply(func, value):
    return func(value)


print("\n--- Functions as values ---")
speak = shout                   # no () - we're not calling it
print(speak("hello"))
print(apply(whisper, "HELLO"))

for style in [shout, whisper]:
    print(style.__name__, "->", style("Python"))

# --- Lambdas -------------------------------------------------------------------------------
print("\n--- Lambdas ---")
double = lambda x: x * 2
print(double(21))

words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words))                          # alphabetical
print(sorted(words, key=lambda w: len(w)))    # by length
print(sorted(words, key=len))                 # same thing - pass the function directly!


# --- Closures --------------------------------------------------------------------------------
def make_counter():
    count = 0

    def increment():
        nonlocal count   # we're reassigning the outer variable
        count += 1
        return count

    return increment


print("\n--- Closures ---")
counter_a = make_counter()
counter_b = make_counter()
print(counter_a(), counter_a(), counter_a())   # 1 2 3
print(counter_b())                             # 1 - separate count


# --- The mutable default trap ------------------------------------------------------------------
def add_item_buggy(item, items=[]):
    items.append(item)
    return items


def add_item_fixed(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print("\n--- Mutable default trap ---")
print(add_item_buggy("a"))   # ['a']
print(add_item_buggy("b"))   # ['a', 'b']  <- the same list was reused!
print(add_item_fixed("a"))   # ['a']
print(add_item_fixed("b"))   # ['b']       <- fresh list each time
