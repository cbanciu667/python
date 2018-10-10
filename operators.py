#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent/100)
    tax = meal_cost * (tax_percent/100)
    total_cost = meal_cost + tip + tax
    print(int(round(total_cost)))

if __name__ == '__main__':
    meal_cost = float(input('Enter meal costs: '))
    tip_percent = int(input('Enter tip percent: '))
    tax_percent = int(input('Enter tax percent: '))

    solve(meal_cost, tip_percent, tax_percent)

# 10.25
# 17
# 5
# expect 13
