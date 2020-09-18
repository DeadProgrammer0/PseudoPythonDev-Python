# Creating our First Class.

from functools import reduce

class student:
    pass

# Here we created three Objects harry, rohan and hamad. Which belongs to Student Class.
harry = student()
rohan = student()
hamad = student()

l1 = [1,34,6,7,8,8,9,1,4]

# These are some variables.
harry.name = "Harry"
harry.std = 12
harry.age = 16
rohan.subjects = ["Maths","Physics","Chemistry"]
rohan.age = harry.age-1
hamad.address = {"Country":"India","State":"Bihar","City":"Patna","Town":"Danapur"}
hamad.MobileNo = "".join(map(str,l1))

print(harry.name)
print(harry.std)
print(harry.age)
print(rohan.subjects)
print(rohan.age)
print(hamad.address)
print(hamad.MobileNo)

# l2 = map(str,l1)
# l3 = str(reduce(lambda x,y: x+y , l2))
