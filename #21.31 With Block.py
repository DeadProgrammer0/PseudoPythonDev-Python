# With Block for File opening.

f = open("test2.txt")
print(f.read())
# You can use With block instead of this.

with open("test2.txt") as f:
    a = f.readlines()
    print(a)

