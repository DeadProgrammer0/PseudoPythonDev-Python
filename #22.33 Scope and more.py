# Scope, Global Variables and Global keyword.


l = 10 # l is in Global Scope. Global Scope means the value of the variable will be same in the whole program.
       # Until there is not a Local variavle determined with the same name.

def func1(n):
    l = 5 # l is in Local Scope. Local Scope means the value of the variable is only for the respective function and it's nested functions.
    m = 8 # m is a local variable thus the variable doesn't have its value determined globally so if you run outside of the function this will give error.
    print(l,m)
    print(n,"Here is your Statement.")

func1("Test 1")


# You can see here m was in local Scope so using m outside of func1 results as an Error.

try:
    print(m)
except Exception as e:
    print("Error!",e)


# Global keyword.

a = 10
b = 20
c = 30

def func2():
    try:
        a = a + 10
    except Exception as e:
        print("Error!",e)
    
    # As you can see you can't change the Globally Scoped variable in a function.
    # But you can change Localy scoped variable.
    b = 25 #Local
    b = b + 5
    print(b)

    # But if you want to change the variable you can use Global keyword.

    global c  
    c = 21
    print(c)

func2()



# This is example that shows if the variable is defined in a function then it can not be changed in its nested functions.
# If you use global keyword then The variable will be changed Globally not in the Parent Function.
# Nested Function means Functions inside Functions.

def harry():

    x = 10
    def rohan():
        global x
        x = 5
    print("Before calling Rohan",x)
    rohan()
    print("After calling Rohan",x)

harry()


# If you'll print x outside the value will we what it was defined earlier by using Global keyword.

print(x)