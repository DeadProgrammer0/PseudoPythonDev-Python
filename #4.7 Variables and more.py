# Variables, Datatypes and Typecasting

# Variables - Variables are Containers of Datatypes or Name allocated to specifice Datatypes.

"""
All DataTypes in Python:- 

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

"""

a = 10
b = "Harry"
c = 5.5

# We can identify Data type of the Variable by using  type() .

print(type(a))  
print(type(b))
print(type(c))


# Concateneting Strings

str1 = 'Hello World '
str2 = 'Harry.'

print(str1+str2)

# TypeCasting - This is used to Type cast one Datatype to another.

var1 = "10"
var2 = "5"

# If we run this print command we'll not get the sum of two variables we'll get a concatenation.
print(var1+var2)

# If we want the sum of the variables we have to  typecast the variables first.
print(int(var1)+int(var2))


# If you want to print a statement multiple times you can simply do this.
print(10*"Hello World\n")

# If the statement is Integer then.
print(10*str(5*9))


# Input - This is used to take inputs from user.

ab = str(input("Enter your Word : "))

print(f"Your word was {ab}")


# Quiz 1

print("\nSimple Calculator\n")
dig1 = int(input("Enter the First Digit : "))
dig2 = int(input("Enter the Second Digit : "))
sum1 = dig1+dig2

print(f"Sum of {dig1} and {dig2} = {sum1}")