"""
@file mathlib.py
@brief File containing math library.

@author
- Vojtěch Gajdušek (xgajduv00)
- Martin Valapka (xvalapm00)
@date March 23, 2024
"""

def add(num1, num2):
    """
    Function to add two numbers.
    
    Parameters:
    num1: First number.
    num2: Second number.
    
    Returns:
    Sum of numbers num1 and num2.
    """
    return num1 + num2

def sub(num1, num2):
    """
    Function to subtract two numbers.

    Parameters:
    num1: First number.
    num2: Second number.
    
    Returns:
    Difference of numbers num1 and num2 (num1 - num2).
    """
    return num1 - num2

def mul(num1, num2):
    """
    Function to multiply two numbers.
    
    Parameters:
    num1: First number.
    num2: Second number.
    
    Returns:
    Product of num1 and num2 (num1 * num2).
    """
    return num1 * num2

def div(dividend, divisor, precision=10):
    """
    Function to divide two numbers.
    
    Parameters:
    dividend (float): The number to be divided (numerator).
    divisor (float): The number by which the dividend is divided (denominator).
    precision (int): Number of decimal places for rounding. Defaults to 10.
    
    Returns:
    float: The quotient of dividend divided by divisor.
    
    Raises:
    ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    result = quotient + (remainder / divisor)
    
    return round(result, precision)

def mod(dividend, divisor):
    """
    Function to compute the modulo operation.
    
    Parameters:
    dividend: The number to be divided.
    divisor: The number by which the dividend is divided.
    
    Returns:
    The remainder after dividing dividend by divisor.
    
    Raises:
    ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend % divisor

def abs(num):
    """
    Function to calculate the absolute value of a number.
    
    Parameters:
    num: The input number.
    
    Returns:
    The absolute value of the input number.
    """
    if num < 0:
        return -num
    else:
        return num

def fac(n: int) -> int:
    """
    Function to compute the factorial of a non-negative integer.
    
    Parameters:
    n (int): The non-negative integer.
    
    Returns:
    int: The factorial of the input integer.
    
    Raises:
    ValueError: If the input is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def pow(base: int, exponent: int) -> int:
    """
    Function to compute the power of a number.
    
    Parameters:
    base (int): The base number.
    exponent (int): The exponent.
    
    Returns:
    int: The result of raising base to the power of exponent.
    """
    if base == 0 and exponent <= 0:
        raise ValueError("Base must be non-zero when the exponent is non-positive.")
    
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def root(number: float, n: int, precision: float = 0.0001) -> float:
    """
    Function to compute the nth root of a number using Newton's method.
    
    Parameters:
    number (float): The number whose root is to be calculated.
    n (int): The root to be calculated (e.g., 2 for square root).
    precision (float): The desired precision of the result. Defaults to 0.0001.
    
    Returns:
    float: The nth root of the given number.
    """
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of negative number.")
        
    if number == 0:
        return 0
    
    x = number / 2
    while abs(x ** n - number) > precision:
        x -= (x ** n - number) / (n * x ** (n - 1))
        
    return x
