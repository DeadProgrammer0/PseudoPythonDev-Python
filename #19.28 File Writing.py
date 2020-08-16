# File Writing in Python.


# This statement is called File Pointer or File Handler.
# f = open("test2.txt","w") # Here we selected writing mode by addind "w".
# But use Write mode only when you want to clear the file's data and rewrite everytime.

# If you want to add new data to the file with previous data to stay then use "a" i.e. used for append.

# f = open("test2.txt","a") # Here we selected appending mode by addind "a".


# f.write("This is A test.\n")

# If you want to count the letters you entered in the file then use

# a = f.write("This is A test.\n")
# print(a)

# If you want to open a file for both reading and writing then use "r+"

f = open("test2.txt","r+")  # Here we selected Reading and Writing mode by addind "r+".
print(f.read())

f.write("Test was Successful.")

f.close() # Always Close the file you Opened.