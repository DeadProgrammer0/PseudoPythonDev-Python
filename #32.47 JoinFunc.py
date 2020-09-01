l1 = ["John Cena","Randy Orton","Roman Reing","UnderTaker"]

# We want to join every Item with and.

# Using For Loop.

for i in l1:
    print(f" {i} and",end="")

# Using Join Function.

print(end="\n")

a = " and ".join(l1)
print(a)