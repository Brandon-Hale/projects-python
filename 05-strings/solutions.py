"""
05 - Strings: solutions
There's usually more than one right answer. If yours passes, it's right!
Run me:  python solutions.py
"""


def shout(text):
    return text.upper() + "!"


def initials(full_name):
    result = ""
    for word in full_name.split():
        result += word[0].upper() + "."
    return result
    # one-liner (you'll learn this style in module 10):
    # return "".join(word[0].upper() + "." for word in full_name.split())


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def capitalise_words(sentence):
    words = []
    for word in sentence.split(" "):
        words.append(word[:1].upper() + word[1:])   # word[:1] is safe even for ""
    return " ".join(words)


def format_price(amount):
    return f"${amount:,.2f}"


def censor(text, word):
    return text.replace(word, "*" * len(word))


def parse_csv_line(line):
    values = []
    for part in line.split(","):
        values.append(part.strip())
    return values


def print_box(text):
    border = "+" + "-" * (len(text) + 2) + "+"
    print(border)
    print(f"| {text} |")
    print(border)


# =============================================================================
# CHECKS - run this file with:  python solutions.py
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
