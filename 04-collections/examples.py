"""
04 - Collections: examples
Run me:  python examples.py
"""

# --- Lists -------------------------------------------------------------------
print("--- Lists ---")
nums = [3, 1, 4]
nums.append(1)
print("after append:", nums)
nums.extend([5, 9])
print("after extend:", nums)
nums.insert(0, 0)
print("after insert(0, 0):", nums)
nums.remove(1)                 # removes the FIRST 1
print("after remove(1):", nums)
last = nums.pop()
print("popped:", last, "->", nums)
print("len:", len(nums))
print("4 in nums?", 4 in nums)
print("index of 4:", nums.index(4))

print("sorted copy:", sorted(nums), "original:", nums)
result = nums.sort()           # sorts in place...
print("nums.sort() returned:", result, "-> nums is now", nums)  # ...and returns None!

# --- Indexing & slicing ---------------------------------------------------------
print("\n--- Slicing ---")
letters = ["a", "b", "c", "d", "e"]
print("letters[0]    =", letters[0])
print("letters[-1]   =", letters[-1])
print("letters[1:3]  =", letters[1:3])
print("letters[:2]   =", letters[:2])
print("letters[2:]   =", letters[2:])
print("letters[-2:]  =", letters[-2:])
print("letters[::2]  =", letters[::2])
print("letters[::-1] =", letters[::-1])

# Slice assignment replaces part of a list
letters[1:3] = ["B", "C"]
print("after slice assignment:", letters)

# --- Tuples -------------------------------------------------------------------------
print("\n--- Tuples ---")
point = (3, 4)
x, y = point
print("x:", x, "y:", y)
single = (5,)
not_a_tuple = (5)
print(type(single).__name__, type(not_a_tuple).__name__)
# point[0] = 10   # <- uncomment: TypeError, tuples are immutable

# Extended unpacking with *
first, *middle, last = [1, 2, 3, 4, 5]
print("first:", first, "middle:", middle, "last:", last)

# --- Dictionaries --------------------------------------------------------------------
print("\n--- Dicts ---")
ages = {"ada": 36, "alan": 41}
ages["grace"] = 85
print(ages)
print("ada:", ages["ada"])
print("get bob:", ages.get("bob"))
print("get bob with default:", ages.get("bob", 0))
print("'ada' in ages?", "ada" in ages)

for name in ages:
    print(" key:", name)
for name, age in ages.items():
    print(f" {name} is {age}")

print("keys:", list(ages.keys()))
print("values:", list(ages.values()))

del ages["alan"]
print("after del:", ages)

# Counting with a dict - a very common pattern
counts = {}
for word in ["red", "blue", "red", "green", "red"]:
    counts[word] = counts.get(word, 0) + 1
print("counts:", counts)

# Tuples can be dict keys, lists can't
grid = {(0, 0): "start", (2, 3): "treasure"}
print("at (2, 3):", grid[(2, 3)])

# --- Sets --------------------------------------------------------------------------------
print("\n--- Sets ---")
a = {1, 2, 3, 4}
b = {3, 4, 5}
print("a | b =", a | b)
print("a & b =", a & b)
print("a - b =", a - b)
print("dedupe:", set([1, 1, 2, 2, 3]))
print("type of {}:", type({}).__name__, "| type of set():", type(set()).__name__)

# --- enumerate & zip -----------------------------------------------------------------------
print("\n--- enumerate & zip ---")
names = ["ada", "alan", "grace"]
scores = [90, 85, 99]

for i, name in enumerate(names):
    print(i, name)

for position, name in enumerate(names, start=1):
    print(f"{position}. {name}")

for name, score in zip(names, scores):
    print(name, "scored", score)

print("as dict:", dict(zip(names, scores)))

# --- Sorting with key -----------------------------------------------------------------------
print("\n--- Sorting ---")
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, reverse=True))
people = [("ada", 36), ("alan", 41), ("grace", 85), ("linus", 21)]
print("by age:", sorted(people, key=lambda person: person[1]))
print("longest word:", max(words, key=len))

# --- References vs copies ---------------------------------------------------------------------
print("\n--- References ---")
original = [1, 2]
alias = original
alias.append(3)
print("original after changing alias:", original)
copy = original.copy()
copy.append(4)
print("original after changing copy:", original, "copy:", copy)
