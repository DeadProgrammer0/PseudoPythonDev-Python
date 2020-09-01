# Map , Filter and Reduce Function.

# Map Function.

l1 = ["2","5","4","3","8"]

# # Using For loop.
# for i in range(len(l1)):
#     l1[i] = int(l1[i])

# Using Map Function

l= list(map(int,l1))

plus = l[1]+5
print(plus)

# Creating list of Squares.

l2 = [1,3,5,7,8,35,2]

# def sq(n):
#     return n*n

# square = list(map(sq , l2))
# print(square)

# square = list(map(lambda x:x*x , l2))
# print(square)

# Creating Tuple of Square, Cube.

def square(n):
    return n*n

def cube(n):
    return n*n*n

func1 = [square , cube]

for i in range(5):
    i += 1
    val = tuple(map(lambda x:x(i),func1))
    print(val)


# Filter Function

def isgreater5(n):
    return 5<n

l2 = [2,34,6,76,1,4,57,5,7,3,4,11]

greater = list(filter(isgreater5,l2))
print(greater)


# Filtering Prime Numbers

from functools import reduce

def factors(n):    
    return list(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

a1 = [*range(1,101)]

def prime(n):
    if n == 1:
        return False
    if factors(n).__len__() == 2:
        return True
    else:
        return False

prime_finder = list(filter(prime , a1))
print(prime_finder)

# Reduce Function

l5 = [1,6,7,8,78]

total = reduce(lambda x,y : x+y,l5)

print(total)

maxz = reduce(lambda x,y: x if x>y else y,l5)

print(maxz)


# Printing Total Exam marks and CGP using Reduce Function.

lis2 = []
subjects = ["Maths","Physics","Chemistry","English","CS"]

for i in subjects:
    lis2.append(int(input(f"Enter your {i} Marks : ")))

total2 = reduce(lambda x,y : x+y ,lis2)
print(f"Your Total Marks out of 500 = {total2}.")

lis3 = [total2,0]

cgp = (reduce(lambda x,y: (x+y)/5,lis3))
print(f"Your Total CGP out of 100% = {cgp}%.")