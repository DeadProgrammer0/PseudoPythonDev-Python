# Else with Loops.

Khaana = ["Roti","Chawal","Sabzi"]

for i in Khaana:
    if i == "Roti":
        print("Your Item is in list.")
        break

else: 
    print("Your Item was not in list.")

def has_even(l):
    for i in l:
        if i%2 == 0:
            print("Has a Even Numbers.")
            break
    else:
        print("No Even Number was Found.")

has_even([1,2,3,4,5])
has_even([1,3,5,7])

count = 0

while count<5:
    count += 1
    print(count)
    break

else:
    print("No Break")