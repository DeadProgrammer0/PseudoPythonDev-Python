print("Welcome! This is a Calculator.\n")

d1 = int(input("Enter the First Digit : "))
d2 = int(input("Enter the Second Digit : "))

op = int(input("\nEnter 1 to Add.\nEnter 2 to Subtract.\nEnter 3 to Multiply.\nEnter 4 to Divide.\nEnter Here = "))



if op == 1:
    print("\nInitializing Calculator For Addition.")
    if d1 == 56 and d2 == 9:
        print(f"{d1} + {d2} = 77")
    else:    
        print(f"{d1} + {d2} =",d1 + d2) 
    

elif op == 2:
    print("\nInitializing Calculator For Substraction.")
    print(f"{d1} - {d2} =",d1 - d2)

elif op == 3:
    print("\nInitializing Calculator For Multiplication.")
    if d1 == 45 and d2 == 3:
        print(f"{d1} * {d2} = 555")
    else:    
        print(f"{d1} * {d2} =",d1 * d2)
    

elif op == 4:
    print("\nInitializing Calculator For Division.")
    if d1 == 56 and d2 == 6:
        print(f"{d1} / {d2} = 4")
    else:    
        print(f"{d1} / {d2} =",d1 / d2) 
    
      

else:
    print("\nInvalid Input!\n")

print("Thanks For Using this Calculator.")