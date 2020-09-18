# Object Introspection



class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{self.fname}.{self.lname}@codewithharry.com"

    def explain(self):
        print(f"The first name is {self.fname} and The last name is {self.lname}.")

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "No Email available."
        else:
            return f"{self.fname}.{self.lname}@codewithharry.com"


    # Setter 
    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    # Deleter
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


skillf = Employee("Skill","f")

# Getting Type of the Object
print(type(skillf))
print(type("Hello"))

# Getting the Unique Id of object. That changes on every save.
print(id("Nice"))

# Getting all methods and attributes of th object.

op = [1,2,3,4,5,6]

# print(dir(op))
# print(dir("ST"))
# print(dir(skillf))


import inspect

print(inspect.getmembers(skillf))