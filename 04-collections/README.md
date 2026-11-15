# 04 · Collections

Python's four built-in collection types (`list`, `tuple`, `dict`, `set`), plus slicing,
`enumerate`, `zip`, and sorting.

**Files:** [`examples.py`](examples.py) · [`exercises.py`](exercises.py) · [`solutions.py`](solutions.py)

---

## The big four at a glance

| Python | Literal | Ordered? | Mutable? | Duplicates? | C# | TS |
|--------|---------|----------|----------|-------------|----|----|
| `list` | `[1, 2, 3]` | ✅ | ✅ | ✅ | `List<T>` | `T[]` |
| `tuple` | `(1, 2, 3)` | ✅ | ❌ | ✅ | `ValueTuple` / `ImmutableArray` | `readonly [..]` tuple |
| `dict` | `{"a": 1}` | ✅ (insertion order) | ✅ | keys unique | `Dictionary<K,V>` | `Record` / `Map` |
| `set` | `{1, 2, 3}` | ❌ | ✅ | ❌ | `HashSet<T>` | `Set` |

Collections can hold **mixed types**: `[1, "two", 3.0]` is fine (though rarely a good idea).

## Lists

```python
nums = [3, 1, 4]
nums.append(1)          # [3, 1, 4, 1]          C#: Add
nums.extend([5, 9])     # [3, 1, 4, 1, 5, 9]    C#: AddRange
nums.insert(0, 0)       # insert at index 0
nums.remove(1)          # removes FIRST 1 (by value)
last = nums.pop()       # remove & return last item
first = nums.pop(0)     # remove & return item at index 0
len(nums)               # length (not .Count / .length!)
4 in nums               # membership test -> True/False
nums.index(4)           # position of first 4
nums.sort()             # sorts IN PLACE, returns None
sorted(nums)            # returns a NEW sorted list
nums.reverse()          # in place
```

### Indexing and slicing

```python
letters = ["a", "b", "c", "d", "e"]
letters[0]      # "a"
letters[-1]     # "e"            negative = from the end
letters[1:3]    # ["b", "c"]     [start:stop], stop excluded
letters[:2]     # ["a", "b"]     from the start
letters[2:]     # ["c", "d", "e"] to the end
letters[::2]    # ["a", "c", "e"] every 2nd item
letters[::-1]   # reversed copy
letters[:]      # shallow copy
```

Slicing works on lists, tuples, and strings.

## Tuples

```python
point = (3, 4)
x, y = point            # unpacking
single = (5,)           # one-item tuple needs a trailing comma
```

Tuples are **immutable**. Use them for fixed groups of values like coordinates, return values,
and dictionary keys.

## Dictionaries

```python
ages = {"ada": 36, "alan": 41}
ages["grace"] = 85              # add / update
ages["ada"]                     # 36
ages["bob"]                     # KeyError!
ages.get("bob")                 # None (no error)
ages.get("bob", 0)              # 0 (default value)
"ada" in ages                   # True (checks KEYS)
del ages["alan"]                # remove

for name in ages:               # loops over KEYS
for name, age in ages.items():  # keys AND values (like KeyValuePair)
ages.keys(), ages.values()
```

Keys must be **immutable** (str, int, tuple, ...). A list can't be a key.

## Sets

```python
tags = {"python", "code"}
tags.add("fun")
tags.discard("code")            # remove if present, no error
a | b      # union
a & b      # intersection
a - b      # difference
set([1, 1, 2])                  # {1, 2}  quick de-duplication
empty = set()                   # NOT {} (that's an empty dict!)
```

## enumerate and zip

```python
for i, name in enumerate(["ada", "alan"]):           # index + value
    print(i, name)                                    # 0 ada / 1 alan

for i, name in enumerate(["ada", "alan"], start=1):  # count from 1

for name, age in zip(["ada", "alan"], [36, 41]):     # walk two lists together
    print(name, age)

dict(zip(names, ages))                               # build a dict from two lists
```

> **C#:** `enumerate` ≈ LINQ `.Select((x, i) => ...)`, `zip` ≈ `.Zip()`.

## Sorting with a key

```python
sorted(words)                         # alphabetical
sorted(words, key=len)                # by length
sorted(people, key=lambda p: p[1])    # by second item
sorted(nums, reverse=True)            # descending
max(words, key=len)                   # longest word
```

## Useful built-ins

`len`, `sum`, `min`, `max`, `sorted`, `reversed`, `any`, `all`, `list()`, `set()`, `dict()`, `tuple()`.

## ⚠️ References, not copies

```python
a = [1, 2]
b = a           # b is the SAME list
b.append(3)
print(a)        # [1, 2, 3]

c = a.copy()    # or a[:] or list(a): a new (shallow) copy
```

Same behaviour as reference types in C# and arrays/objects in TS.

---

## Gotchas for C#/TS developers

1. `len(x)`, not `x.length` or `x.Count`.
2. `list.sort()` returns `None`. Use `sorted(list)` if you want the result.
3. `{}` is an empty **dict**. Use `set()` for an empty set.
4. `dict["missing"]` raises `KeyError`. Use `.get()` when the key might be absent.
5. Slices exclude the stop index, same as `range`.

## Your turn

Open [`exercises.py`](exercises.py), complete each function, and run `python exercises.py`.
