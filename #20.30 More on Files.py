# Seek() and Tell() functions.



f = open("test2.txt")


print(f.tell()) # Tell() Function is used to find the current location of the file pointer i.e. "f" here.
print(f.readline(),end="")
f.seek(24) # Seek() Function is used to move the file pointer.
print(f.tell())
print(f.readline(),end="")
print(f.tell())
print(f.readline(),end="")
print(f.tell())
print(f.readline(),end="")

f.close()