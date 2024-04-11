"""
@file mathlib.py
@brief File containing math library.

@author
- Vojtěch Gajdušek (xgajduv00)
@date April 11, 2024
"""

# IMPORTS
import math
from decimal import Decimal, getcontext

def add(num1, num2):
    """
    @brief Function to add two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Sum of numbers num1 and num2.
    """
    result = math.fsum([num1, num2])
    return round(result, 10)

def sub(num1, num2):
    """
    @brief Function to subtract two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Difference of numbers num1 and num2 (num1 - num2).
    """
    result = num1 - num2
    return round(result, 10)

def mul(num1, num2):
    """
    @brief Function to multiply two numbers.
    
    @param num1: First number.
    @param num2: Second number.
    
    @return Product of num1 and num2 (num1 * num2).
    """
    getcontext().prec = 28
    num1_dec = Decimal(str(num1))
    num2_dec = Decimal(str(num2))
    result = num1_dec * num2_dec
    if isinstance(num1, int) and isinstance(num2, int):
        return int(result)
    else:
        return float(result)

def div(dividend, divisor):
    """
    @brief Function to divide two numbers.
    
    @param dividend: The number to be divided (numerator).
    @param divisor: The number by which the dividend is divided (denominator).
    
    @return The quotient of dividend divided by divisor.
    
    @exception ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    
    dividend_dec = Decimal(str(dividend))
    divisor_dec = Decimal(str(divisor))
    result = dividend_dec / divisor_dec
    if isinstance(dividend, int) and isinstance(divisor, int) and result % 1 == 0:
        return int(result)
    else:
        return float(result)

def mod(dividend, divisor):
    """
    @brief Function to compute the modulo operation.
    
    @param dividend: The number to be divided.
    @param divisor: The number by which the dividend is divided.
    
    @return The remainder after dividing dividend by divisor.

    @exception ValueError: If the divisor is zero.
    """
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    dividend_decimal = Decimal(str(abs(dividend)))
    divisor_decimal = Decimal(str(abs(divisor)))

    remainder = dividend_decimal % divisor_decimal
    if divisor < 0:
        remainder = -remainder
    return float(remainder)

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

    @exception ValueError: If the input is negative.
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
    
    if not isinstance(exponent, int):
        raise ValueError("Exponent must be an integer.")
    
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    
    if base == 0 and exponent == 0:
        raise ValueError("0^0 is undefined.")

    result = base ** exponent

    if result >= 1e100:
        return float('inf')
    else:
        return result

def root(number: float, n: int) -> float:
    """
    @brief Function to compute the nth root of a number using Newton's method.
    
    @param number: The number whose root is to be calculated.
    @param n: The root to be calculated (e.g., 2 for square root).
    
    @return Nth root of the given number.
    """
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot compute even root of negative number.")
        
    if number == 0:
        return 0
    
    getcontext().prec = 50
    number_decimal = Decimal(str(number))
    x = number_decimal / 2
    tolerance = Decimal('0.0000000001')
    while abs(x ** n - number_decimal) > tolerance:
        x -= (x ** n - number_decimal) / (n * x ** (n - 1))
        
    result_decimal = x
    if isinstance(number, int) and isinstance(n, int):
        return int(result_decimal)
    else:
        return float(result_decimal)

