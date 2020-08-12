# String Slicing And Other Functions In Python.

# String Slicing 
# In python index start from 0.

mystr = "Harry is a good boy"
#This String Contains 20 alphabets starting from 0.


print(mystr.__len__())

# String Slicing is done like this by adding [ : : ] .
print(mystr[0:19:1])


# By default String Slicing Values are [ 0 : End of The String : 1 ]
# [1:10:2] in this "1" the beginning is included but "10" the ending is excluded.
# And the third digit "2" the stepping is used to leave steps in the string.
# In simple representation [ Start : End : Step ]

# We can use Negative Digit for Slicing too.
# image - https://qph.fs.quoracdn.net/main-qimg-a380b1bc159589df5e0b9842e5b56b6d

print(mystr[-3:])

# A easy way to reverse string
print(mystr[::-1])

print(mystr[-8:-4])

# String Functions 

# Refference = https://www.w3schools.com/python/python_ref_string.asp

mystr2 = "This is Just a regular sentence."


print(mystr2.isalnum())
print(mystr2.isalpha())
print(mystr2.endswith("sentence."))
print(mystr2.count("e"))
print(mystr2.__len__())
print(mystr2.upper())
print(mystr2.lower())
print(mystr2.find("i"))
print(mystr2.replace("a",""))
print(mystr2.islower())
print(mystr2.isnumeric())
