# Function Decorators 

def func1(n):
    print("Here :",n)

func2 = func1
del func1

func2("Hello")

def funcret(num):
    
    if num == 0:
        return min
    if num == 1:
        return max 
    else:
        return

a = funcret(1)
print(a)


def executer(func):
    func("This")

executer(print)


def dec1(func1):
    def nowexec():
        print("Executing")
        func1()
        print("Done")
    return nowexec()

def Who_is_harry():
    print("Harry is good boy.")

Who_is_harry = dec1(Who_is_harry)

def is_called():
    def is_returned():
        print("Hello")
    return is_returned()

new = is_called

new()


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

pretty = make_pretty(ordinary)
pretty()



@dec1
def ordinary2():
    print("Ordinary 2")


a1 = int(input())
b1= int(input())  

def better_divide(func1):
    def inner(a,b):
        print(f"Dividing {a1} and {b1}.")
        if b == 0:
            print("Invalid.")
            return
        return func1(a,b)
    return inner

@better_divide
def divide(a, b):
    print(a//b)
  

divide(a1,b1)


def star(func):
    def inner(*args,**kwargs):
        print("*"*30)
        func(*args,**kwargs)
        print("*"*30)
    return inner


def hash(func):
    def inner(*args,**kwargs):
        print("#"*30)
        func(*args,**kwargs)
        print("#"*30)
    return inner

@star
@hash
def multiple(name):
    print(name)

multiple("Hello World")