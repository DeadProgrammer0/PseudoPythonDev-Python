# For Loops in Python.
# For Loops can be only used on Iterative Datatypes like List, Tuple, String.


# Using For loop on List.

l1 = ["Aman","Nitish","Kunal","Rohan"]

for i in l1:
    print(i)

# Using For loop on List of List.

l2 = [["Amam",75],["Nitish",95],["Kunal",40],["Rohan",80]]

print("\n")

for i,j in l2:
    print(f"{i} got {j} in last Test.")

# Using For loop on Dictionary.

dic1 = dict(l2)
print("\n")

for key,value in dic1.items():
    print(f"{key} got {value} in last Test.")


print("\n")

for i in dic1:
    print(i)

print("\n")

# Quiz 3 

l3 = [1,2,54,5,7908,0,2,11,"kik","lol","nic","s"]

for i in l3:
    if str(i).isnumeric() and i>6:
        print(i)


            