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