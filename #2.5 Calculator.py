# Using Python as Calculator.
# We can do normal Arithmatic Caculation in Python by using Arihematic Operators.

print(5+5)
print(10-5)
print(5*2)
print(10/2)
print(2+2-2*2/2)


# Flexing Time

print("This is a Simple Calculator.\n")
a = int(input("Enter your First Digit : "))
b = int(input("Enter your Second Digit : "))

c = int(input("\nEnter 1 for Addition.\nEnter 2 for Subtraction.\nEnter 3 for Multiplication.\nEnter 4 for Divison.\n"))

if c == 1:
    print(f"Doing Addition : {a} + {b} = {a+b}")

elif c == 2: 
    print(f"Doing Subtraction : {a} - {b} = {a-b}")

elif c == 3:
    print(f"Doing Multiplication : {a} * {b} = {a*b}")

elif c == 4:
    print(f"Doing Division : {a} / {b} = {a/b}")

else:
    print("Error! Something went Wrong.")