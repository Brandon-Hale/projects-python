"""
12 - Testing: examples
Run me:  python examples.py

This file needs NOTHING installed. It shows:
  1. plain assert
  2. the built-in unittest module
For pytest (the usual choice), see test_calculator.py and run `pytest -v`.
"""
import unittest

from calculator import BankAccount, add, average, divide, is_leap_year

# --- 1. Plain assert -----------------------------------------------------------------
print("--- assert ---")
assert add(2, 3) == 5
assert is_leap_year(2000)
assert not is_leap_year(1900)
print("all plain asserts passed")

try:
    assert add(2, 2) == 5, "add(2, 2) should be 5?!"
except AssertionError as error:
    print("a failing assert raises AssertionError:", error)


# --- 2. unittest -----------------------------------------------------------------------
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(9, 3), 3)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

    def test_average(self):
        self.assertAlmostEqual(average([0.1, 0.2]), 0.15)

    def test_leap_years(self):
        cases = {2024: True, 2023: False, 1900: False, 2000: True}
        for year, expected in cases.items():
            with self.subTest(year=year):          # like a parametrised test
                self.assertEqual(is_leap_year(year), expected)


class TestBankAccount(unittest.TestCase):
    def setUp(self):                               # runs before EACH test, like [SetUp]
        self.account = BankAccount(100)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.balance, 70)

    def test_overdraw(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(500)
        self.assertEqual(self.account.balance, 100)


print("\n--- unittest ---")
unittest.main(argv=["examples"], verbosity=2, exit=False)
