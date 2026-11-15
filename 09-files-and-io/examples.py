"""
09 - Files and I/O: examples
Run me:  python examples.py

Reads from the data/ folder next to this file, and writes to a temporary
folder that is deleted at the end (so the repo stays clean).
"""
import csv
import json
import tempfile
from pathlib import Path

HERE = Path(__file__).parent          # works no matter where you run this from
DATA = HERE / "data"

# --- Reading a whole file ---------------------------------------------------------
print("--- read() ---")
with open(DATA / "poem.txt", encoding="utf-8") as f:
    text = f.read()
print(text)

# --- Reading line by line -----------------------------------------------------------
print("--- for line in f ---")
with open(DATA / "poem.txt", encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.rstrip()}")      # rstrip removes the trailing "\n"

print("\n--- readlines() keeps the newlines ---")
with open(DATA / "poem.txt", encoding="utf-8") as f:
    print(f.readlines()[:2])

print("\n--- splitlines() doesn't ---")
print(text.splitlines()[:2])

# --- pathlib shortcuts ------------------------------------------------------------------
print("\n--- pathlib ---")
poem = DATA / "poem.txt"
print("name:", poem.name, "| stem:", poem.stem, "| suffix:", poem.suffix)
print("exists?", poem.exists(), "| size:", poem.stat().st_size, "bytes")
print("word count:", len(poem.read_text(encoding="utf-8").split()))
print("files in data/:", sorted(p.name for p in DATA.iterdir()))

# --- CSV --------------------------------------------------------------------------------------
print("\n--- CSV with DictReader ---")
totals = {}
with open(DATA / "sales.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        amount = float(row["amount"])                  # CSV values are strings!
        totals[row["product"]] = totals.get(row["product"], 0) + amount
for product, total in totals.items():
    print(f"{product:<10} ${total:>7.2f}")

# --- Writing (into a temporary folder) ----------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    out_dir = Path(tmp)
    print("\n--- Writing files (in a temp folder) ---")

    # write mode "w" creates/overwrites
    notes = out_dir / "notes.txt"
    with open(notes, "w", encoding="utf-8") as f:
        f.write("first line\n")                         # write() won't add the \n for you
        f.writelines(["second line\n", "third line\n"])
        print("fourth line via print()", file=f)
    print(notes.read_text(encoding="utf-8"))

    # append mode "a" adds to the end
    with open(notes, "a", encoding="utf-8") as f:
        f.write("appended line\n")
    print("line count now:", len(notes.read_text(encoding="utf-8").splitlines()))

    # pathlib one-liners
    quick = out_dir / "quick.txt"
    quick.write_text("written with pathlib\n", encoding="utf-8")
    print(quick.read_text(encoding="utf-8").strip())

    # Writing CSV
    report = out_dir / "report.csv"
    with open(report, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "total"])
        for product, total in totals.items():
            writer.writerow([product, f"{total:.2f}"])
    print("\nreport.csv:")
    print(report.read_text(encoding="utf-8"))

    # JSON round trip
    settings = {"theme": "dark", "font_size": 14, "recent": ["a.py", "b.py"], "beta": False}
    settings_file = out_dir / "settings.json"
    with open(settings_file, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=2)
    print("settings.json:")
    print(settings_file.read_text(encoding="utf-8"))
    with open(settings_file, encoding="utf-8") as f:
        loaded = json.load(f)
    print("loaded back equals original?", loaded == settings)

    # Folders and globbing
    (out_dir / "sub" / "deeper").mkdir(parents=True, exist_ok=True)
    (out_dir / "sub" / "deeper" / "x.txt").write_text("x", encoding="utf-8")
    print("\nall .txt files (recursive):", sorted(p.name for p in out_dir.rglob("*.txt")))

    # Handling a missing file
    try:
        (out_dir / "missing.txt").read_text(encoding="utf-8")
    except FileNotFoundError as error:
        print("FileNotFoundError:", error.filename)

print("\n(temp folder deleted)")

# --- Console input (commented out so this script doesn't wait for you) -----------------------
# name = input("What's your name? ")
# print(f"Hi {name}!")
