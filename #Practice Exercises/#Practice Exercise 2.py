from typing import Counter


while True:

    try:
        apples = int(input("Enter number of apples : "))
        mn = int(input("Enter minimum number : "))
        mx = int(input("Enter maximum number : "))
    except Exception as e:
        print('Enter integers only!')
        continue
    else:
        if mn > mx:
            print('This can\'t be a range. Minimum should be less than Maximum.')
            continue
        else:
            break

print()
for i in range(mn,mx+1):
    if apples % i == 0:
        print(f"{i} is divisor of {apples}.")

    elif apples % i != 0:
        print(f"{i} is not divisor of {apples}.")

