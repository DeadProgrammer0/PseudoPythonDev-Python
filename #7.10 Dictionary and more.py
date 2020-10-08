# Dictionary & Its Functions Explained

# Dictionary is nothing but KEY : VALUE pairs.
# Dictionary is Contained in Braces {} .

dict1= {"Harry":"Burger","Rohan":"Fish","SkillF":"Roti"}

print(type(dict1))

# We Can Access Dictionary values by their Keys.

try:
    print(dict1["harry"]) 
except Exception as s:
    print(f"Error! {s}.")

# Here we got Error Because Dictionary's Keys and Values are Case Sensetive.

print(dict1["Harry"])
print(dict1["Rohan"])

# We Can also use .get function.
print(dict1.get("Harry"))


# We can also add Dictionary in Dictionary.

dict2 = {"Raj":"Dosa","Shubham":{"B":"Maggie","L":"Rice","D":"Chicken"}}

print(dict2["Shubham"]["L"])

# Dictionary Functions

# Adding New values in Dictionary
dict1["Ankit"] = "Bhindi"

# We can also Add New value by using .update function. And The can also be a number.
dict1.update({420:"Pizza"})
dict1.update({"Harry":"Pasta"})

# We can remove any Value by using del command.
del dict1["Ankit"]

# We Can also make a Copy of the Dictionary by using .copy .

dict3 = dict1.copy()
del dict3["Harry"]

print(dict3)


print(dict1)

# Some more Fuctions.

print(dict1.keys())
print(dict1.values())
print(dict1.items())

