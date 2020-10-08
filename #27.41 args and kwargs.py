# *Args and **Kwargs

def student_name(a,b,c,d):
    k = [a,b,c,d]
    print(f"These are the Students : ")
    for i in k:
        print(i)


student_name("Harry","Rohan","SkillF","Hamad")

# Function student_name() takes only 4 arguments if you exeed the number of arguments the program will give error.

try:
    student_name("Conrflakes","Harry","Rohan","SkillF","Hamad")
except Exception as e:
    print(f"Error! {e}")

# To Avoid this error *args and **kwargs are used.

# *args
# *args take input as lists and tuples only.
# *args always typecasts the input in tuple.

def Vovels(statement,*vovel):
    print(statement)
    for i in vovel:
        print(i)

har = ["a","e","i","o","u"]
state = "These are all vovels : "

Vovels(state,*har)

# **kwargs
# **kwargs accept input only as Dictionary.
# Important Note - The sequence to use *args and **kwargs is (normal,*args,**kwargs)

def student_roles(normal,**kwargs):
    print(normal)
    for key , value in kwargs.items():
        print(f"{key} is a {value}.")
    

har3 = {'Hamad': 'Instructer', 'Rohan': 'Programmer', 'Harry': 'Cook'}
state2 = "These are Student's Roles : "

student_roles(state2,**har3)