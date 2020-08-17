inp = int(input("Enter the Number of rows : "))
m = int(input("Enter 0 for False or 1 for True : "))

m1 = bool(m)

if m1 == True:
    for i in range(1,inp+1): # for Number of Rows
        for j in range(1,i+1): # for Number of Columns
            print("*",end="")
        print()


elif m1 == False:
    for i in range(inp,0,-1): 
        for j in range(1,i+1):
            print("*",end="")
        print()

