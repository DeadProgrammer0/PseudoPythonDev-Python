# Class Methods


def design(func):
    def inner(*args,**kwargs):
        print("-"*30)
        func(*args,**kwargs)
        print("-"*30)
    return inner 

class Employee:

    No_of_leaves = 10
    Office_time = "9 to 5"

    # Claas Methods can be used when you, Don't want Self as a variable. It can be accesse by @classmethod Decorator.
    # It take cls (i.e. is Class) as their first variable.
    # Changing Class variable's values using function.
    @classmethod
    def change(cls,newleave,newtime):
        cls.No_of_leaves = newleave
        cls.Office_time = newtime


    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role


    @design
    def access(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nRole : {self.role}\nNumber of Leaves : {self.No_of_leaves}\nOffice Time : {self.Office_time}")
    
harry = Employee("Harry","70,000","Instructor")
rohan = Employee("Rohan","30,000","Student")
hamad = Employee("Hamad","50,000","Assisstant Manager")


harry.access()
rohan.access()
hamad.access()


harry.change(12,"12 to 6")
print(rohan.No_of_leaves)
print(rohan.Office_time)

