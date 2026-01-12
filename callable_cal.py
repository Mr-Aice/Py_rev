from typing import Callable

def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y

def multiply(x: int, y: int) -> int:
    return x * y

def cal(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)


first_number: int = int(input("Enter first number: "))
second_number: int = int(input("Enter second number: "))

print(
    f"""
Addition: {cal(first_number, second_number, add)}
Subtraction: {cal(first_number, second_number, subtract)}
Multiplication: {cal(first_number, second_number, multiply)}
    """)

