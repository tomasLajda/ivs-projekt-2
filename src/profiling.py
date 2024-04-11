import sys
import mathlib

def seperate_numbers_from_std():
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

  #if len(numbers) < 1000:
  #  print("Error: The list must have at least 1000 numbers.")
  #  sys.exit()
  
  return numbers

def arithmetic_mean(numbers):
  sum = 0
  for number in numbers:
    sum = mathlib.add(sum, number)

  return mathlib.div(sum, len(numbers))

def standard_deviation(numbers):
  mean = arithmetic_mean(numbers)

  sum = 0
  for number in numbers:
    sum = mathlib.add(sum, mathlib.pow(mathlib.sub(number, mean), 2))

  result = mathlib.mul(sum, mathlib.div(1, mathlib.sub(len(numbers), 1)))

  return mathlib.root(result, 2)

numbers = seperate_numbers_from_std()
print(standard_deviation(numbers))