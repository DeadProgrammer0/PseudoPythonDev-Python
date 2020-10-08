# Self and __init__()



def design(func):
    def inner(*args,**kwargs):
        print("-"*30)
        func(*args,**kwargs)
        print("-"*30)
    return inner 

class Employee:

    # Creating Instance variables using Functions.
    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    
    # Accessing variables using a Function.
    # Self is the defualt variable taken by all function that is used in place of Object.
    @design
    def access(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nRole : {self.role}")
    
harry = Employee("Harry","70,000","Instructor")
rohan = Employee("Rohan","30,000","Student")

harry.access()
rohan.access()