dict1 = {"Mutable":"Changeable","Immutable":"Unchangeable","Rescue":"Save Someone",
"Accomplished":"To complete something",
"Worthless":"useless","Suggestion":"Idea"}

print("This is a Simple Dictionary.")

user = str(input("Enter Your Word Here : "))

print("Your Word was :",user.capitalize())



print("Meaning :",dict1.get(user.capitalize()))