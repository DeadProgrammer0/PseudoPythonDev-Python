

mylist = list(eval(input("Enter your list : ")))


#* Method 1 :-
reverse_1 = mylist.copy()
reverse_1.reverse()
print('\nFirst method!')
print(f'The reverse of {mylist} is {reverse_1}.')

#* Method 2 :-
reverse_2 = mylist[::-1]
print('\nSecond method!')
print(f'The reverse of {mylist} is {reverse_2}.')

#* Method 3 :-
reverse_3 = mylist.copy()
temp = mylist.copy()
for i in range(len(mylist)):
    reverse_3[i] = temp[len(reverse_3)-i-1]

#? OR
# reverse_3 = mylist.copy()
# for i in range(len(mylist)//2):
#     reverse_3[i], reverse_3[len(reverse_3) -i -1] = reverse_3[len(reverse_3) -i -1], reverse_3[i]

print('\nThird method!')
print(f'The reverse of {mylist} is {reverse_2}.')