"""
@file mathlib.py
@brief File containing math library.

@author
- Vojtěch Gajdušek (xgajduv00)
@date April 11, 2024
"""

def add(num1, num2):
    """
    @brief Function to add two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Sum of numbers num1 and num2.
    """
    return num1 + num2

def sub(num1, num2):
    """
    @brief Function to subtract two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Difference of numbers num1 and num2 (num1 - num2).
    """
    return num1 - num2

def mul(num1, num2):
    """
    @brief Function to multiply two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Product of num1 and num2 (num1 * num2).
    """
    return num1 * num2

def div(dividend, divisor, precision=10):
    """
    @brief Function to divide two numbers.
    
    @param dividend (float): The number to be divided (numerator).
    @param divisor (float): The number by which the dividend is divided (denominator).
    @param precision (int): Number of decimal places for rounding. Defaults to 10.
    
    @return The quotient of dividend divided by divisor.
    
    //TODO: @throws ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    result = quotient + (remainder / divisor)
    
    return round(result, precision)

def mod(dividend, divisor):
    """
    @brief Function to compute the modulo operation.
    
    @param dividend: The number to be divided.
    @param divisor: The number by which the dividend is divided.
    
    @return The remainder after dividing dividend by divisor.
    //TODO:
    Raises:
    ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    return dividend % divisor

def abs(num):
    """
    @brief Function to calculate the absolute value of a number.
    
    @param num: The input number.
    
    @return The absolute value of the input number.
    """
    if num < 0:
        return -num
    else:
        return num

def fac(n: int) -> int:
    """
    @brief Function to compute the factorial of a non-negative integer.
    
    @param n: The non-negative integer.
    
    @return The factorial of the input integer.
    //TODO:
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
    @brief Function to compute the power of a number.
    
    @param base: The base number.
    @param exponent: The exponent.
    
    @return The result of raising base to the power of exponent.
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    
    if base == 0 and exponent == 0:
        raise ValueError("0^0 is undefined.")
    
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def root(number: float, n: int, precision: float = 0.0001) -> float:
    """
    @brief Function to compute the nth root of a number using Newton's method.
    
    @param number: The number whose root is to be calculated.
    @param n: The root to be calculated (e.g., 2 for square root).
    @param precision: The desired precision of the result. Defaults to 0.0001.
    
    @return The nth root of the given number.
    """
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of negative number.")
        
    if number == 0:
        return 0
    
    x = number / 2
    while abs(x ** n - number) > precision:
        x -= (x ** n - number) / (n * x ** (n - 1))
        
    return x
