# File Reading in Python.

f = open("test.txt","rt") # The second argument in open() is for mode i.e. "rt" here. "rt" is Default mode.
                          # Which opens file for reading in Text mode. 


# content = f.read()
# print(content)

# content = f.read(21)
# print("1",content, end="")

# content = f.read(20)
# print("2",content)

# If you want to read the file Line by line then you can do this 

# for line in f:
#     print(line,end="")

# You can Itrate lines like this or you can use functions like readline and readlines

# content = f.readline()
# print(content)
# This is used to read Line by Line.

content2 = f.readlines()
print(content2)
# This is used to show all the lines in a list.





f.close()