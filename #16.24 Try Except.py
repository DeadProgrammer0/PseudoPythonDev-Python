# Try Except Exception Handling.


try:
    a = int(input("Enter First Number : ")) 
    b = int(input("Enter Second Number : "))

    print("The Sum of Two Numbers =",a+b)

except Exception as e:
    print("Error!",e)


print("This is an Important Line.")
