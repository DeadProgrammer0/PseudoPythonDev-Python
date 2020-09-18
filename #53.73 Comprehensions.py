# Python Comprehensions.

# List Comprehensions.

l1 = []

for i in range(1,100):
    if i%3 == 0:
        l1.append(i)


l2 = [i for i in range(1,100) if i%3 == 0 ]

print(l1)
print(l2)

# Dictionary Comprehensions.

dic1 = {}
dic3 = {}

for i in range(11):
    dic1.update({i:f"Item {i}"})

for i,j in dic1.items():
    dic3.update({j:i})
    

dic2 = {
    i:f"Item {i}" for i in range(11)
}

dic4 = {
    j:i for i,j in dic2.items()
}

print(dic1)
print(dic3)
print(dic2)
print(dic4)

# Set Comprehensions


dresses = { i for i in ["Dress 1","Dress 2","Dress 3","Dress 2","Dress 3"]}

print(dresses)

# Generator Comprehensions

Evens = ( i for i in range(99) if i%2 == 0)

Even = [ i for i in Evens]
print(Even)














l = []
mat = [[1,2,3],[4,5,6]]
mat2 = [[1, 2], [3,4], [5,6], [7,8]]

for i in range(len(mat[0])):
    lm = []

    for item in mat:
        lm.append(item[i])
    l.append(lm)

l2 = [[item[i] for item in mat2] for i in range(2)]
l3 = [[item[i] for item in mat2] for i in range(2)]

