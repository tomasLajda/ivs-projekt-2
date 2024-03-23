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

def div(dividend, divisor):
    """
    Function to divide two numbers.
    
    Parameters:
    dividend: The number to be divided.
    divisor: The number by which the dividend is divided.
    
    Returns:
    Quotient of num1 divided by num2 (num1 / num2).
    
    Raises:
    ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend / divisor

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
    result = 1
    for _ in range(exponent):
        result *= base
    return result