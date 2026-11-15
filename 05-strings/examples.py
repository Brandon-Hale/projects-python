"""
05 - Strings: examples
Run me:  python examples.py
"""

# --- Creating strings ------------------------------------------------------------
print("--- Creating ---")
a = 'single'
b = "double"
c = """triple quoted
strings can
span lines"""
path = r"C:\new\folder"       # raw string - \n is NOT a newline here
print(a, b)
print(c)
print(path)
print("escapes: tab[\t] newline[\\n] quote[\"]")

# --- Indexing & slicing ---------------------------------------------------------------
print("\n--- Indexing & slicing ---")
word = "python"
print(word[0], word[-1], word[1:4], word[::-1], len(word))
print("'th' in word?", "th" in word)
print("type of word[0]:", type(word[0]).__name__)   # str - there is no char type
print("ord('A') =", ord("A"), "| chr(97) =", chr(97))

# word[0] = "P"   # <- uncomment: TypeError, strings are immutable
capitalised = "P" + word[1:]
print("new string:", capitalised)

# --- Methods ---------------------------------------------------------------------------
print("\n--- Methods ---")
messy = "   Hello, World!   "
print(f"[{messy.strip()}]")
print(f"[{messy.lstrip()}]")
print(messy.strip().upper())
print(messy.strip().lower())
print(messy.strip().replace("World", "Python"))
print("hello world".title())
print("hello world".capitalize())
print("banana".count("a"))
print("banana".find("n"), "banana".find("z"))   # -1 when not found
print("report.pdf".endswith(".pdf"), "report.pdf".startswith("rep"))
print("12345".isdigit(), "abc".isalpha(), "abc1".isalnum(), "   ".isspace())
print("42".zfill(5))

# Methods return NEW strings
s = "quiet"
s.upper()
print("s is still:", s)
s = s.upper()
print("now s is:", s)

# --- split & join -------------------------------------------------------------------------
print("\n--- split & join ---")
csv_line = "ada,alan,grace"
names = csv_line.split(",")
print(names)
print("  hello   world  ".split())          # whitespace split, no empties
print("a,b,,c".split(","))                  # keeps the empty string
print(" | ".join(names))
numbers = [1, 2, 3]
print(", ".join(str(n) for n in numbers))    # items must be strings
print("key=value=more".split("=", 1))        # max 1 split

# --- f-string formatting ---------------------------------------------------------------------
print("\n--- Formatting ---")
name, price, qty = "Widget", 1234.5, 7
print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{qty:03}")
print(f"[{name:>10}]")
print(f"[{name:<10}]")
print(f"[{name:^10}]")
print(f"[{name:*^10}]")    # custom fill character
print(f"{0.256:.1%}")
print(f"{name!r}")
print(f"{qty=}")            # debug shortcut
print(f"{255:x} {255:b}")   # hex and binary

# A simple aligned table
rows = [("Apples", 3, 0.5), ("Bananas", 12, 0.25), ("Cherries", 100, 0.1)]
print(f"{'Item':<10}{'Qty':>5}{'Price':>8}")
for item, quantity, unit_price in rows:
    print(f"{item:<10}{quantity:>5}{unit_price:>8.2f}")

# --- Building strings with join -------------------------------------------------------------------
print("\n--- Building strings ---")
parts = []
for n in range(5):
    parts.append(str(n * n))
print("-".join(parts))

# Repetition
print("=" * 20)
print("ab" * 3)

# --- Looping over characters ------------------------------------------------------------------------
print("\n--- Looping ---")
vowels = 0
for ch in "Programming in Python":
    if ch.lower() in "aeiou":
        vowels += 1
print("vowels:", vowels)

for i, ch in enumerate("hey"):
    print(i, ch)

# --- str vs repr ----------------------------------------------------------------------------------------
print("\n--- str vs repr ---")
text = "line one\nline two"
print(str(text))
print(repr(text))   # shows the \n - great for debugging whitespace issues
