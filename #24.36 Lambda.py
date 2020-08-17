# Lambda Functions or Anonymous Functions.

# Lambda Functions are just for convenience similar to Short Hand If Else.

# Defining normal functions.

def sum(a,b):
    return a + b

print(sum(2,5))

# Definig Lambda functions.

minus = lambda a,b : a-b

print(minus(6,4))

# More Example.

a = [[13,2],[4,54],[66,7]]

# def a_first(a):
#     return a[1]


a.sort(key=lambda x: x[1])
print(a)

# Creating a filter for printing only Odd numbers.

b = [24,5,66,80,78,2,72,88,9,3,55,997]

odd = list(filter( lambda x : (x%2 != 0) , b))

print(odd)


# Creating a filter for printing only Even numbers.


even = list(filter(lambda x:(x%2==0),b))

print(even)

# Doubling every numberin the list.

double = list(map(lambda x:(x*2),b))

print(double)