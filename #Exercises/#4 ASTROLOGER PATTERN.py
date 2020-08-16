inp = int(input("Enter Number of Rows : "))

m = int(input("Enter 0 for False or 1 for True : "))
m1 = bool(m)
print("You choosed",m1)

if m1 == True:    
    for i in range(1,inp+1):
        print()
        for j in range(1,i+1):
            print("*",end="")

elif m1 == False:
    for i in range(inp+1,0,-1):
        print()
        for j in range(i+1,1,-1):
            print("*",end="")