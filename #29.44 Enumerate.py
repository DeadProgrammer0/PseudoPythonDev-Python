
# Enumerate Function.

l1 = ["Bhindi","Aloo","Chopsticks","Chowmien"]

# We want only 1 and 3 item of the list.

i = 1
for item in l1:
    if i%2 != 0:
        print(f"Bring {item}")
    i += 1


for index,item in enumerate(l1):
    if index%2 == 0:
        print(f"Bring {index}. {item}")




