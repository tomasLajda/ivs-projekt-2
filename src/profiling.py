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

  if len(numbers) < 1000:
    print("Error: The list must have at least 1000 numbers.")
    sys.exit()
  
  return numbers

numbers = seperate_numbers_from_std()