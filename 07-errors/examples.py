"""
07 - Errors: examples
Run me:  python examples.py
"""

# --- Basic try / except ------------------------------------------------------------
print("--- try / except ---")
for text in ["42", "abc"]:
    try:
        number = int(text)
        print(f"{text!r} -> {number}")
    except ValueError as error:
        print(f"{text!r} -> ValueError: {error}")

# --- Every part: except / else / finally -----------------------------------------------
print("\n--- except / else / finally ---")


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  {a}/{b}: can't divide by zero")
        return None
    except TypeError as error:
        print(f"  {a}/{b}: wrong type - {error}")
        return None
    else:
        print(f"  {a}/{b}: worked, result {result}")
        return result
    finally:
        print(f"  {a}/{b}: finally always runs")


divide(10, 2)
divide(10, 0)
divide(10, "2")

# Catching several types at once
print("\n--- multiple types ---")
for value in ["7", None, "x"]:
    try:
        print(int(value) * 2)
    except (ValueError, TypeError) as error:
        print(f"couldn't double {value!r}: {type(error).__name__}")

# --- Common built-in exceptions ---------------------------------------------------------------
print("\n--- Common exceptions ---")
experiments = [
    lambda: int("abc"),                # ValueError
    lambda: "a" + 1,                   # TypeError
    lambda: {"a": 1}["b"],             # KeyError
    lambda: [1, 2, 3][10],             # IndexError
    lambda: None.upper(),              # AttributeError
    lambda: 1 / 0,                     # ZeroDivisionError
    lambda: open("does-not-exist.txt"),  # FileNotFoundError
]
for experiment in experiments:
    try:
        experiment()
    except Exception as error:
        print(f"{type(error).__name__:<18} {error}")

# --- Raising ------------------------------------------------------------------------------------
print("\n--- Raising ---")


def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"age must be an int, got {type(age).__name__}")
    if age < 0:
        raise ValueError("age can't be negative")
    return age


for age in [30, -5, "old"]:
    try:
        print("set age:", set_age(age))
    except (TypeError, ValueError) as error:
        print("rejected:", error)


# --- Custom exceptions --------------------------------------------------------------------------
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""

    def __init__(self, balance, amount):
        super().__init__(f"tried to withdraw {amount} but balance is only {balance}")
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


print("\n--- Custom exceptions ---")
try:
    withdraw(50, 80)
except InsufficientFundsError as error:
    print("Error:", error)
    print("Short by:", error.shortfall)


# --- Re-raising and chaining ---------------------------------------------------------------------
class ConfigError(Exception):
    pass


def read_setting(settings, key):
    try:
        return settings[key]
    except KeyError as error:
        raise ConfigError(f"missing setting {key!r}") from error


print("\n--- Chaining ---")
try:
    read_setting({"debug": True}, "port")
except ConfigError as error:
    print("ConfigError:", error)
    print("caused by:", repr(error.__cause__))

# --- EAFP vs LBYL ----------------------------------------------------------------------------------
print("\n--- EAFP vs LBYL ---")
settings = {"theme": "dark"}

# LBYL
if "font" in settings:
    font = settings["font"]
else:
    font = "default"
print("LBYL font:", font)

# EAFP
try:
    font = settings["font"]
except KeyError:
    font = "default"
print("EAFP font:", font)

# Best for dicts
print(".get font:", settings.get("font", "default"))

# --- finally for cleanup --------------------------------------------------------------------------
print("\n--- finally cleanup ---")


def process(should_fail):
    print("  opening resource")
    try:
        if should_fail:
            raise RuntimeError("something broke")
        print("  working...")
    finally:
        print("  closing resource")   # runs either way


process(False)
try:
    process(True)
except RuntimeError as error:
    print("  caught:", error)
