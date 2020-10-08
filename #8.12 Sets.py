# A set is a collection of well-defined objects and non-repetitive elements
# That is - a set with 1,2,3,4,3,4,5,2, 2, and 3 as its elements can be written as {1,2,3,4,5}

s = {13,2,5}

print(type(s))

# We can use list in Set.

l=[1,2,12,5,6]
s1 = set(l)

print(s1)

# Adding Values in Set.

s2 = set({3,45})

s2.add(2)
s2.add(21)
s2.add(1)
s2.add(2)

print(s2)


# s3 = s2.union({2,1,26,6,12})
# s3 = s2.intersection({2,1,26,6,12})
# s3 = s2.isdisjoint({2,1,26,6,12})
# print(s3)

s2.remove(2)
print(s2)

