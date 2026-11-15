"""
02 - Control flow: examples
Run me:  python examples.py
"""

# --- if / elif / else --------------------------------------------------------
print("--- if / elif / else ---")
temperature = 22

if temperature > 30:
    print("Hot")
elif temperature > 15:
    print("Nice")       # <- this one runs
else:
    print("Cold")

# Chained comparisons read like maths
if 18 <= temperature <= 25:
    print("Perfect temperature")

# Logic uses words
is_weekend = True
is_raining = False
if is_weekend and not is_raining:
    print("Go outside!")

# Ternary / conditional expression
age = 20
label = "adult" if age >= 18 else "minor"
print("label:", label)

# `pass` is a placeholder for an empty block
if age > 100:
    pass  # TODO: handle centenarians

# --- Truthiness ----------------------------------------------------------------
print("\n--- Truthiness ---")
for value in [0, 1, "", "hi", "0", [], [0], None, {}, 0.0, "False"]:
    result = "truthy" if value else "falsy"
    print(f"{value!r:>8} is {result}")   # !r shows the repr, :>8 right-aligns

name = ""
if not name:
    print("name is empty")

# Checking for None: use `is`
result = None
if result is None:
    print("no result yet")

# --- for loops with range ---------------------------------------------------------
print("\n--- for + range ---")
for i in range(5):
    print(i, end=" ")        # 0 1 2 3 4
print()

for i in range(1, 6):
    print(i, end=" ")        # 1 2 3 4 5
print()

for i in range(0, 20, 5):
    print(i, end=" ")        # 0 5 10 15
print()

for i in range(5, 0, -1):
    print(i, end=" ")        # 5 4 3 2 1
print()

# for-each over a string and a list
for letter in "hey":
    print(letter.upper(), end="")
print()

for fruit in ["apple", "banana", "cherry"]:
    print("I like", fruit)

# Accumulating a total
total = 0
for n in range(1, 11):
    total += n
print("sum of 1..10 =", total)

# --- while loops -----------------------------------------------------------------
print("\n--- while ---")
count = 3
while count > 0:
    print("count:", count)
    count -= 1
print("done")

# "do-while" style: loop forever, break when done
attempts = 0
while True:
    attempts += 1
    if attempts >= 3:
        break
print("attempts:", attempts)

# --- break / continue ------------------------------------------------------------
print("\n--- break / continue ---")
for n in range(10):
    if n % 2 == 0:
        continue   # skip even numbers
    if n > 7:
        break      # stop completely
    print("odd:", n)

# --- loop else -----------------------------------------------------------------------
print("\n--- for / else ---")
numbers = [4, 8, 15, 16, 23, 42]
for n in numbers:
    if n > 40:
        print("found one over 40:", n)
        break
else:
    print("nothing over 40")  # only runs if we never hit `break`

for n in numbers:
    if n > 100:
        print("found one over 100:", n)
        break
else:
    print("nothing over 100")

# --- match ------------------------------------------------------------------------------
print("\n--- match ---")
for command in ["start", "quit", "dance"]:
    match command:
        case "start":
            print(command, "-> Starting")
        case "stop" | "quit":
            print(command, "-> Stopping")
        case _:
            print(command, "-> Unknown command")

# match can also destructure (a taste of what's possible)
point = (0, 5)
match point:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f"on the y axis at y={y}")
    case (x, 0):
        print(f"on the x axis at x={x}")
    case (x, y):
        print(f"somewhere else: {x}, {y}")
