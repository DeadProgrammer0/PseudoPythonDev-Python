# Python Lists And List Functions

# Python lists are containers used to store a list of values of any data type.
# In simple words, we can say that a list is a collection of any data type items or elements.

lsit1 = [4.5,"Hello",1,2,3]
# List is Contained in Square Brackets [].
# List can hold different Data types.
# We can access List items Like Shown Below:-

print(lsit1[1])
# Index in Lists also Strats from 0.


# List Slicing 
# List Slicing is Simillar to String Slicing.

l2 = [2,3.5,8,7,66,4]

print(l2[2::-1])

# We Can use Negative Integers too as same as Strings.
# But its preffered not to use less than -1 in stepping in both strings and lists.


# List Functions.
# Let's see Some List functions.

l3 = [21,436,789,4,1,22,3,12.3]

# l3.sort() # Sorts the List.
# l3.reverse() # Reverse the Lsit.

print(max(l3)) # Prints max value.
print(min(l3)) # Prints min value.
print(len(l3)) # Prints Length.

l3.append(0.5) # Adds the value to end of the List.
print(l3)

l3.insert(2,5) # Inserts value at given Index.
print(l3)

l3.remove(4) # Removes given  Value.
print(l3)

# Tuple
# Tuples are contained in Parenthesis ().

# Mutable = Can Change.
# Immutable = Can't Change.

# Lists are Mutable.
# And Tuples are Immutable We can't Change Tuple's value.

tp1 = (1,23,6,9)
print(tp1)

"""
try:
    tp1.sort()
except Exception as s:
    print(f"Error! {s}.")
"""

# Off Topic

"""

A = 1
B = 2

A , B = B , A
print(A , B)


a =1
b =3

temp =a
a = b
b =temp
print(a,b)

"""