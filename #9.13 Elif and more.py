# If , Elif And Else in Python
# If, else and elif statement can be defined as a multiway decision taken by our program due to the certain conditions in our code.


# A simple Program that take input from user and compare the input to the previous data.
# And Prints the Statement. 

var1 = 10

var2 = int(input("Enter Your Number : "))

if var1>var2:
    print("Lesser")

elif var1 == var2:
    print("Equal")

else:
    print("Greater")    


# A simple Program for checking wheather the value is in list or not.

l1 = [1,3,5,7,9,11,13,15]

user = int(input("Enter a Number : "))

if user  in l1:
    print("It's in the List")

elif user not in l1:
    print("It's not in List")
    ab = int(input("If you want to add the number press 1.\n"))
    
    if ab == 1:
        l1.append(user)
        print("Your Number is added.")
        print(l1)
    else:
        print("Program Ended.")

# Quiz 2


age = 18

print("\nThis is Driving Test Program If you want a Driving Licence You've to above 18 and under 75.\n")
user2 = int(input("Enter your age : "))

if user2>75:
    print("You are too old for the licence.")

elif user2>age:
    print("Your age is Perfect for the licence.")

elif user2<age:
    print("You are currently Underaged for a licence.")

elif user2 == age:
    print("You are 18. We are not sure of your driving skills.\nPlease come for a Driving test.")

else:
    print("Enter a Valid Age!")


print("\nThanks For applying.")


