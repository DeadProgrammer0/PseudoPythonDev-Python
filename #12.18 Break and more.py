# Break and Continue Statement.

i = 0
 
while(1):
    if i < 10:
        i = i + 1
        continue

    i = i + 1
    print(i , end=" ")
    if i == 45:
        break


# Quiz 4. 

print("Please Enter a number Greater than 100.")
while(1):
    ip = int(input("Enter Here : "))
    if ip>100:
        print("Congratulation! You have entered a Number greater than 100.")
        break

    elif ip<=100:
        print("Please enter a number Greater than 100.")
        continue

    else:
        print("Error! Invalid Input.")