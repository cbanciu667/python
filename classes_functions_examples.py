# FUNCTION that plays around with odd and even variables
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if (N > 1) and (N < 100):
      reminder = N%2
      #print(reminder)
      if reminder != 0:
        print('Weird')
      elif (N >= 2) and (N <= 5) and (reminder == 0):
        print('Not Weird')
      elif (N >= 6) and (N <= 20) and (reminder == 0):
        print('Weird')
      elif (N >= 20) and (reminder == 0):
        print('Not Weird')
    else:
        print('Out of range')

# CLASS example - age variables
class Person:
    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        # print(initialAge)
        if initialAge < 0:
            Person.age = 0
            print('Age is not valid, setting age to 0.')
        else:
            Person.age = initialAge
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if (Person.age) < 13:
            print('You are young.')
        elif (Person.age >= 13) and (Person.age < 18):
            print('You are a teenager.')
        else: print('You are old.')
    def yearPasses(self):
        # Increment the age of the person in here
        Person.age = Person.age + 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


# CLASS vehicle - car variables
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.name = 'Fer'
car1.kind = 'convertible'
car1.color = 'red'
car1.value = 60000.00

car2.name = 'Jump'
car2.kind = 'van'
car2.color = 'blue'
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())
