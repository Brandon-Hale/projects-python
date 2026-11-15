"""
08 - Modules and packages: examples
Run me from THIS folder:  python examples.py
"""

# --- Importing our own module (string_tools.py, in this folder) -----------------
import string_tools
from string_tools import slugify, truncate as shorten

print("--- Our own module ---")
print(string_tools.slugify("Hello World, From Python!"))
print(slugify("Another  Example__Here", separator="_"))
print(shorten("This sentence is far too long", 15))
print("module name inside string_tools:", string_tools.__name__)
print("module name of this file:", __name__)   # "__main__" because we ran it directly

# --- Importing from our own package (the shapes/ folder) ------------------------
from shapes import circle_area, square_area     # re-exported by shapes/__init__.py
from shapes import circle                       # a module inside the package
from shapes.square import perimeter

print("\n--- Our own package ---")
print("circle area r=2:", round(circle_area(2), 2))
print("square area s=3:", square_area(3))
print("circumference r=1:", round(circle.circumference(1), 2))
print("square perimeter s=3:", perimeter(3))

# --- Standard library tour -------------------------------------------------------
print("\n--- math ---")
import math
print(math.sqrt(16), math.pi, math.floor(2.7), math.ceil(2.1), math.isclose(0.1 + 0.2, 0.3))

print("\n--- random ---")
import random
rng = random.Random(42)            # seeded so the output is the same every run
print(rng.randint(1, 6), rng.choice(["rock", "paper", "scissors"]))
deck = list(range(1, 6))
rng.shuffle(deck)
print("shuffled:", deck)

print("\n--- datetime ---")
from datetime import date, datetime, timedelta
launch = date(1969, 7, 20)
print("launch:", launch, "| weekday:", launch.strftime("%A"))
print("a week later:", launch + timedelta(days=7))
print("days between:", (date(1970, 1, 1) - launch).days)
print("parsed:", date.fromisoformat("2024-02-29"))
print("now (varies):", datetime.now().strftime("%Y-%m-%d %H:%M"))

print("\n--- collections ---")
from collections import Counter, defaultdict, namedtuple
words = "the cat and the hat and the bat".split()
counts = Counter(words)
print(counts)
print("most common 2:", counts.most_common(2))

by_letter = defaultdict(list)       # missing keys get an empty list automatically
for word in words:
    by_letter[word[0]].append(word)
print(dict(by_letter))

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p, p.x, p.y)

print("\n--- itertools ---")
import itertools
print(list(itertools.combinations("ABC", 2)))
print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.chain([1, 2], [3], [4, 5])))
print(list(itertools.islice(itertools.count(10, 5), 4)))   # first 4 of an infinite sequence

print("\n--- json ---")
import json
data = {"name": "Ada", "languages": ["Python", "C#"], "active": True, "manager": None}
text = json.dumps(data, indent=2)
print(text)                               # note: True -> true, None -> null
back = json.loads(text)
print(back["languages"])

print("\n--- pathlib ---")
from pathlib import Path
here = Path(__file__).parent              # the folder this file lives in
print("this folder:", here.name)
print("python files here:", sorted(p.name for p in here.glob("*.py")))
report = Path("reports") / "2024" / "summary.txt"   # / joins paths
print(report, "| suffix:", report.suffix, "| stem:", report.stem)

print("\n--- sys ---")
import sys
print("python version:", sys.version.split()[0])
print("script arguments:", sys.argv)
