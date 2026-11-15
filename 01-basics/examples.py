"""
01 - Basics: examples
Run me:  python examples.py
Then change things and run me again!
"""

# --- Variables -------------------------------------------------------------
# No var/let/const. Just assign. The VALUE has a type, the variable doesn't.
name = "Ada"
age = 36
height = 1.68
is_admin = False
nothing = None  # Python's null

print("--- Variables ---")
print(name, age, height, is_admin, nothing)

# type() tells you what type a value is
print(type(name), type(age), type(height), type(is_admin), type(nothing))

# You CAN reassign a different type (legal, but confusing - avoid it)
age = "thirty-six"
print("age is now:", age, type(age))
age = 36  # put it back

# --- Numbers ---------------------------------------------------------------
print("\n--- Numbers ---")
print("7 + 2  =", 7 + 2)
print("7 - 2  =", 7 - 2)
print("7 * 2  =", 7 * 2)
print("7 / 2  =", 7 / 2)    # 3.5  -> / is ALWAYS float division
print("7 // 2 =", 7 // 2)   # 3    -> floor (integer) division
print("7 % 2  =", 7 % 2)    # 1    -> remainder
print("7 ** 2 =", 7 ** 2)   # 49   -> power
print("-7 // 2 =", -7 // 2) # -4   -> rounds DOWN, not toward zero like C#

# Integers never overflow
print("2 ** 100 =", 2 ** 100)

# Underscores make big numbers readable
population = 8_100_000_000
print("population:", population)

# No ++ or --. Use += and -=
count = 0
count += 1
count += 1
count -= 1
print("count:", count)

# Floats have the usual floating point quirks
print("0.1 + 0.2 =", 0.1 + 0.2)
print("rounded:", round(0.1 + 0.2, 2))

# --- Strings and f-strings ---------------------------------------------------
print("\n--- Strings ---")
single = 'single quotes'
double = "double quotes"  # identical meaning
print(single, "|", double)

# f-strings: put f before the quote, expressions go in {}
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")
print(f"Height to 1 decimal place: {height:.1f}")
print(f"Padded number: [{age:5}]")     # width 5
print(f"Zero padded: {7:03}")           # 007
print(f"Thousands: {population:,}")     # 8,100,000,000

# print() options
print("a", "b", "c")             # separated by spaces
print("a", "b", "c", sep="-")    # custom separator
print("no newline after this...", end="")
print(" see?")

# --- Booleans ----------------------------------------------------------------
print("\n--- Booleans ---")
print(True and False)  # and / or / not instead of && || !
print(True or False)
print(not True)
print(5 > 3, 5 == 5.0, 5 != 4)

# --- Type conversion -----------------------------------------------------------
print("\n--- Conversion ---")
print(int("42") + 1)        # str -> int
print(float("3.5") * 2)     # str -> float
print(str(99) + " bottles") # int -> str
print(int(3.99))            # float -> int truncates: 3
print(round(3.5), round(4.5))  # 4 4 -> "banker's rounding", same as C# default!

# This would crash - uncomment to see the error:
# print("Age: " + age)   # TypeError: can only concatenate str (not "int") to str

# isinstance() checks a type (like C# `is`)
print(isinstance(42, int), isinstance("42", int))

# --- Multiple assignment ---------------------------------------------------------
print("\n--- Multiple assignment ---")
x, y = 1, 2
print("before swap:", x, y)
x, y = y, x  # swap without a temp variable
print("after swap: ", x, y)

a = b = 0
print("a and b:", a, b)

# --- Constants (by convention only) ------------------------------------------------
MAX_USERS = 100  # UPPER_CASE means "please don't change me". Nothing enforces it.
print("\nMAX_USERS:", MAX_USERS)
