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
      num = int(numberString)
      numbers.append(num)
    except ValueError:
      print(f"Error: '{numberString}' isn't a number.")
      sys.exit()

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

  sum = 0
  for number in numbers:
    sum = mathlib.add(sum, mathlib.pow(mathlib.sub(number, mean), 2))

  result = mathlib.mul(sum, mathlib.div(1, mathlib.sub(len(numbers), 1)))

  return mathlib.root(result, 2)

numbers = seperate_numbers_from_std()
print(standard_deviation(numbers))
