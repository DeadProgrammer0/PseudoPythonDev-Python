# Yield and Generators.

def facto(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        yield fac

# for i in facto(40):
#     print(i)

def fibu(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        yield a
    # return a

for i in fibu(6):
    print(i)


