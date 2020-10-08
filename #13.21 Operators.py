# Operators In python.
# Arithmetic Operators
# Assignment Operators
# Comparison (Relational) Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators



#1 Arithmetic Operators.
#There are 7 Arithmetic Operators.
# + Addition = Adds values on either side of the operator.
# - Subtraction = Subtracts right hand operand from left hand operand.
# * Multiplication = Multiplies values on either side of the operator.
# / Division = Divides left hand operand by right hand operand.
# % Modulus = Divides left hand operand by right hand operand and returns remainder.
# ** Exponent =	Performs exponential (power) calculation on operators.
# // Floor Division = The division of operands where the result is the quotient in which the digits after the decimal point are removed. But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity). 

print("Arithmetic Operators")
print("5 + 10:" , 5+10 )
print("10 - 5:" , 10-5 )
print("5 * 10:" , 5*10 )
print("27 / 5:" , 27/5)
print("11 % 5:" , 11%5)
print("5 ** 3:" , 5**3)
print("27 // 5:" , 27//5)

#2 Assignment Operator.
# There are 8 Assignment Operator.

a = 21
b = 10
c = 0
# =	  - Assigns values from right side operands to left side operand|	c = a + b assigns value of a + b into c
# +=  Add AND - It adds right operand to the left operand and assign the result to left operand|	c += a is equivalent to c = c + a
# -=  Subtract AND - It subtracts right operand from the left operand and assign the result to left operand|	c -= a is equivalent to c = c - a
# *=  Multiply AND - It multiplies right operand with the left operand and assign the result to left operand|	c *= a is equivalent to c = c * a
# /=  Divide AND - It divides left operand with the right operand and assign the result to left operand|	c /= a is equivalent to c = c / a
# %=  Modulus AND - It takes modulus using two operands and assign the result to left operand|	c %= a is equivalent to c = c % a
# **= Exponent AND - Performs exponential (power) calculation on operators and assign value to the left operand| c **= a is equivalent to c = c ** a
# //= Floor Division - It performs floor division on operators and assign value to the left operand|	c //= a is equivalent to c = c // a

print("Assignment Operators")

c = a+b
print("c = a+b: " , c )
c += a
print("c+= a: " , c)
c -= a
print("c-= a: " , c)
c *= a
print("c*= a: " , c)
c /= a
print("c/= a: " , c)

c  = 2
c %= a
print("c%= a: " , c)
c **= a
print("c**= a: " , c )
c //= a
print("c//= a: " , c )

#3 Comparison (Relational) Operators.
#There are 6 Comparison Operators.

# ==  -  If the values of two operands are equal, then the condition becomes true.                               	       (a == b) is not true.
# !=  -  If values of two operands are not equal, then condition becomes true.                               	           (a != b) is true.
# >	  -  If the value of left operand is greater than the value of right operand, then condition becomes true.             (a > b) is not true.
# <	  -  If the value of left operand is less than the value of right operand, then condition becomes true.                (a < b) is true.
# >=  -  If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. (a >= b) is not true.
# <=  -  If the value of left operand is less than or equal to the value of right operand, then condition becomes true.    (a <= b) is true.# 

print("Comparison operators")
print( a == b)
print(a != b)
print(a  >  b)
print (a  < b)
print( a  <=  b)
print(a  >= b)


#4 Logical Operators

p = 10
q = 20

# and -Logical AND	-If both the operands are true then condition becomes true.	
# or  -Logical OR	-If any of the two operands are non-zero then condition becomes true.	
# not -Logical NOT	-Used to reverse the logical state of its operand.

a = False
b = True

print("Logical Operators")
print(  a and b)
print(not b or a)
print( not a and b)

#5 Identity Operators.
# There are 2 Identity Operators.

# is	Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.	
# is not	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.

print("Identity Operators")
print(5 is 5)
print(5 is not 5)


#6 Membership Operators.
# There two Membership Operators.

# in	 -  Evaluates to true if it finds a variable in the specified sequence and false otherwise.
# not in -	Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

l1 = [1,25,99,45,5,47,2]

print("Membership Operators")
print(25 in l1)
print(2 not in l1)


#7 Bitwise Operators.
#There are 6 Bitwise Operators.

# & Binary AND	Operator copies a bit to the result if it exists in both operands
# | Binary OR	It copies a bit if it exists in either operand.
# ^ Binary XOR	It copies the bit if it is set in one operand but not both.
# ~ Binary Ones Complement	It is unary and has the effect of 'flipping' bits.
# << Binary Left Shift	The left operands value is moved left by the number of bits specified by the right operand.
# >> Binary Right Shift	The left operands value is moved right by the number of bits specified by the right operand.

print("Bitwise Operators")




