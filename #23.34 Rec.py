# Recursions: Recursive Vs Iterative Approach

# Recursion means calling the function in itself.

# Let's See a Example of Factorial.

# Factorial Formula - n! = n * n-1!

# Recursive Method.

def Factorial_rec(n):
    
    if n == 0 or n == 1:
        return 1

    else:
        return n* Factorial_rec(n-1)

inp = int(input("Enter your Number to find Factorial : "))

print(f"Recursive. Your Factorial is {Factorial_rec(inp)}")

# Benefit of using Recursive method is that you can use maths formula directly.

# Itrative Method.

def Factorial_it(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)

    return fac 


print(f"Itrative. Your Factorial is {Factorial_it(inp)}")


# Quiz 

# Fibunacci Sequence
# Formula - n = n-1 + n-2

def Fibunacci_rec(n):
    if n<2:
        return n

    else:
        return Fibunacci_rec(n-1) + Fibunacci_rec(n-2)

inp2 = int(input("Enter your number for Fibunacci Sequence : "))

print(f"Recursive. The Fibunacci of your is {Fibunacci_rec(inp2)}")


def Fibunacci_it(n):
    f0 = 0 
    f1 = 1
    for i in range(n):
        f0,f1 = f1 , f0+f1
        
    return f0

print(f"Itrative. The Fibunacci of your is {Fibunacci_it(inp2)}")

