# Printing Hello World in Python.

print("Hello World")

# Printing Hello World in Python with Some Flexing.

ip = int(input("Enter 1 to print Hello World or Enter 0 to type your own Word.\n"))

if ip == 1:
    print("Hello World")

elif ip == 0:
    a = str(input("Enter your Word : "))
    print(f"Your word was {a}.")

else: 
    print("Invalid Input.")



