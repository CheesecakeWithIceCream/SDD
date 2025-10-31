from random import *

numbers = []

def random20numbers():
  for x in range(20):
    numbers.append(randrange(1,51))
  return numbers

def displayNumbers (numbers):
  for x in range(20):
    print  (numbers[x]," ",end="")

def findingMax(numbers):
  max = numbers[0]
  for index in range(1,len(numbers)):
    if numbers[index] > max:
      max = numbers[index]
  print()
  print("The highest number (maximum) in the list is",max,".")

numbers = random20numbers()
displayNumbers(numbers)
findingMax(numbers)