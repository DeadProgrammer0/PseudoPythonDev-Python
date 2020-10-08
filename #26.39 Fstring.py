# F Strings.

# F string was Addition in Python 3.6

# String formatting without F strings.


# Method 1 

a = "Harry"
b = 3

c = "This is %s %s"%(a,b)

print(c)

# Method 2

a1 = "Rohan"
b1 = 4
c1 = "Hello World {0} {1}"

d = c1.format(a1,b1)
print(d)


# Using F strings.

print(f"This is {a} and {a1}.")

# You can also do calculations in Fstrings.

print(f"4 + 6 = {4+6}")

# You can use Functions in Fstrings.

import math

print(f"Cos of 65 = {math.cos(65)}")

# F strings make your programming fast and increase Readablity.
# F strings stands for Fast Strings.