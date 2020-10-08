# Using Python Built-in and Random Functions.

# Random Module.
# Refference - https://www.w3schools.com/python/module_random.asp


import random

# Generates random number between given a and b.
random_number = random.randint(2,29)

print(random_number)

# Generates Random number between 0 and 1. if you want to increase the number then multiply by the number you want to.
rand = random.random() * 20

print(rand)

vovels = ("a","e","i","o","u")

# Chooses a random value from given List or Tuple.
choice = random.choice(vovels)

print(choice)


# Some more modules.  

import math

inp = int(input("Enter your number for Factorial : "))

# A function for taking out Factorial.
factorial = math.factorial(inp)

print(f"This is you Factorial = {factorial}")


print(math.isnan(math.pi))
print(math.isnan(math.e))
print(math.isnan(math.nan))

# Date and Time module.


import datetime

# Creates custom Date and Time.
date = datetime.datetime(2005,11,9,12,00)

print(date)

# Returns the current Date and Time.
now = datetime.datetime.now()

print(now)


