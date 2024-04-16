"""
@file profiling.py
@brief File containing profiling.

@author
- Tomáš Lajda (xlajdat00)
@date April 11, 2024
"""

import sys
import mathlib

def seperate_numbers_from_std():
  """
  @brief Reads input from standard input and separates the numbers.
  
  @return A list of integers extracted from the input.
  
  @throws SystemExit If the input contains a non-numeric value.
  """
  inputString = sys.stdin.read()

  numbersString = inputString.split()

  numbers = []

  for numberString in numbersString:
    try:
      num = float(numberString)
      numbers.append(num)
    except ValueError:
      print(f"Error: '{numberString}' isn't a number.")
      sys.exit(1)

  return numbers

def arithmetic_mean(numbers):
  """
  @brief Calculates the arithmetic mean of a list of numbers.
  
  @param numbers A list of numbers.
  
  @return The arithmetic mean of the numbers.
  """
  sum = 0
  for number in numbers:
    sum = mathlib.add(sum, number)

  return mathlib.div(sum, len(numbers))

def standard_deviation(numbers):
  """
  @brief Calculates the standard deviation of a list of numbers.
  
  @param numbers A list of numbers.
  
  @return The standard deviation of the numbers.
  """
  if len(numbers) == 1:
    return 0
  
  mean = arithmetic_mean(numbers)
  mean = mathlib.mul(mathlib.pow(mean, 2), len(numbers))

  sum = 0
  for number in numbers:
    sum = mathlib.add(sum, mathlib.pow(number, 2))

  sum = mathlib.sub(sum, mean)

  result = mathlib.root(mathlib.mul(sum, mathlib.div(1, mathlib.sub(len(numbers), 1))), 2)

  return result

numbers = seperate_numbers_from_std()

try:
  std = standard_deviation(numbers)
  print(std)
except:
  print("Error: Standard deviation couldn't be calculated.")
  sys.exit(1)
