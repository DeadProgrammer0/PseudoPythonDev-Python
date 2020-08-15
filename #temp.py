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