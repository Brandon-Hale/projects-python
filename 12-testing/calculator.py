"""calculator - a small module for test_calculator.py and examples.py to test."""


def add(a, b):
    return a + b


def divide(a, b):
    return a / b      # raises ZeroDivisionError when b == 0


def average(numbers):
    if not numbers:
        raise ValueError("can't average an empty list")
    return sum(numbers) / len(numbers)


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
