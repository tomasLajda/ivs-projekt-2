"""
@file profiling.py
@brief Script to generate inputed number of numbers to data.txt file

@author
- Tomáš Lajda (xlajdat00)
@date April 22, 2024
"""
import random

number = input("Enter a number of random generated numbers: ")

try:
  number = int(number)
except ValueError:
  print("Please enter a valid number")
  exit()

randomNumbers = [random.randint(0, 1000) for _ in range(number)]

with open('../profiling/data.txt', 'w') as f:
  for number in randomNumbers:
    f.write(f'{number}\n')