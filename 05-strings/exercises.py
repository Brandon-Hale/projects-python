"""
05 - Strings: exercises

Delete each `raise NotImplementedError` line, write your code,
then run:  python exercises.py
"""


# ---------------------------------------------------------------------------
# Exercise 1: Shout
# Return the text in upper case with "!" on the end.
#   shout("hello")  ->  "HELLO!"
# ---------------------------------------------------------------------------
def shout(text):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 2: Initials
# Return the initials of a full name, each followed by a dot, in upper case.
#   initials("Ada Lovelace")        ->  "A.L."
#   initials("grace brewster hopper") ->  "G.B.H."
# ---------------------------------------------------------------------------
def initials(full_name):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 3: Palindrome
# Return True if the text reads the same forwards and backwards,
# IGNORING case and spaces.
#   is_palindrome("Race car")  ->  True
#   is_palindrome("hello")     ->  False
# ---------------------------------------------------------------------------
def is_palindrome(text):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 4: Count vowels
# Return how many vowels (a, e, i, o, u - upper or lower case) are in the text.
#   count_vowels("Programming")  ->  3
# ---------------------------------------------------------------------------
def count_vowels(text):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 5: Capitalise each word
# Capitalise the first letter of every word, WITHOUT using .title().
# Words are separated by single spaces. The rest of each word stays as-is.
#   capitalise_words("hello big world")  ->  "Hello Big World"
# ---------------------------------------------------------------------------
def capitalise_words(sentence):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 6: Format a price
# Return the amount as dollars with a thousands separator and 2 decimals.
#   format_price(1234.5)  ->  "$1,234.50"
#   format_price(3)       ->  "$3.00"
# ---------------------------------------------------------------------------
def format_price(amount):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 7: Censor
# Replace every occurrence of `word` in `text` with asterisks of the same length.
#   censor("I love spam and spam", "spam")  ->  "I love **** and ****"
# ---------------------------------------------------------------------------
def censor(text, word):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 8: Parse a CSV line
# Split on commas and strip the whitespace around each value.
#   parse_csv_line(" ada , 36,  London ")  ->  ["ada", "36", "London"]
# ---------------------------------------------------------------------------
def parse_csv_line(line):
    raise NotImplementedError  # delete this line and write your code


# ---------------------------------------------------------------------------
# Exercise 9: Print a box
# PRINT the text inside a box made of "+", "-" and "|", with one space of
# padding on each side of the text.
#   print_box("hi") prints:
#     +----+
#     | hi |
#     +----+
# Hint: "-" * n
# ---------------------------------------------------------------------------
def print_box(text):
    raise NotImplementedError  # delete this line and write your code


# =============================================================================
# CHECKS - run this file with:  python exercises.py
# You don't need to read or edit anything below this line (yet!).
# =============================================================================
import io
from contextlib import redirect_stdout

_checks = []


def check(test):
    _checks.append(test)
    return test


def output_of(func, *args):
    """Run func and return everything it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(*args)
    return buffer.getvalue()


def expect(actual, expected, label):
    assert actual == expected, f"{label} should be {expected!r}, got {actual!r}"


@check
def ex01_shout():
    expect(shout("hello"), "HELLO!", 'shout("hello")')


@check
def ex02_initials():
    expect(initials("Ada Lovelace"), "A.L.", 'initials("Ada Lovelace")')
    expect(initials("grace brewster hopper"), "G.B.H.", 'initials("grace brewster hopper")')


@check
def ex03_is_palindrome():
    expect(is_palindrome("Race car"), True, 'is_palindrome("Race car")')
    expect(is_palindrome("hello"), False, 'is_palindrome("hello")')
    expect(is_palindrome("A man a plan a canal Panama"), True,
           'is_palindrome("A man a plan a canal Panama")')


@check
def ex04_count_vowels():
    expect(count_vowels("Programming"), 3, 'count_vowels("Programming")')
    expect(count_vowels("AEIOU xyz"), 5, 'count_vowels("AEIOU xyz")')
    expect(count_vowels(""), 0, 'count_vowels("")')


@check
def ex05_capitalise_words():
    expect(capitalise_words("hello big world"), "Hello Big World", 'capitalise_words("hello big world")')
    expect(capitalise_words("iPhone mcDonald"), "IPhone McDonald", 'capitalise_words("iPhone mcDonald")')


@check
def ex06_format_price():
    expect(format_price(1234.5), "$1,234.50", "format_price(1234.5)")
    expect(format_price(3), "$3.00", "format_price(3)")
    expect(format_price(1000000), "$1,000,000.00", "format_price(1000000)")


@check
def ex07_censor():
    expect(censor("I love spam and spam", "spam"), "I love **** and ****",
           'censor("I love spam and spam", "spam")')
    expect(censor("no match", "xyz"), "no match", 'censor("no match", "xyz")')


@check
def ex08_parse_csv_line():
    expect(parse_csv_line(" ada , 36,  London "), ["ada", "36", "London"],
           'parse_csv_line(" ada , 36,  London ")')


@check
def ex09_print_box():
    expect(output_of(print_box, "hi"), "+----+\n| hi |\n+----+\n", 'What print_box("hi") printed')
    expect(output_of(print_box, "Python"), "+--------+\n| Python |\n+--------+\n",
           'What print_box("Python") printed')


if __name__ == "__main__":
    passed = 0
    for test in _checks:
        try:
            test()
        except NotImplementedError:
            print(f"[TODO]  {test.__name__}")
        except AssertionError as error:
            print(f"[FAIL]  {test.__name__}: {error}")
        except Exception as error:
            print(f"[ERROR] {test.__name__}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"[PASS]  {test.__name__}")
    print(f"\n{passed}/{len(_checks)} exercises passing")
