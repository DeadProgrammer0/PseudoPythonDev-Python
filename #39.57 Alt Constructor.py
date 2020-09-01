# Class Modules as Alternative Constructor.


def design(func):
    def inner(*args,**kwargs):
        print("-"*30)
        func(*args,**kwargs)
        print("-"*30)
    return inner 

class Employee:

    No_of_leaves = 10
    Office_time = "9 to 5"

    @classmethod
    def change(cls,newleave,newtime):
        cls.No_of_leaves = newleave
        cls.Office_time = newtime

    # Using Class Method as an Alternative Constructor.
    # This function accepts the Values Given to the Class (i.e. Employee("Name-Salary-Role") here)
    # And Converts it to a List.
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    def __init__(self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role

    @design
    def access(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nRole : {self.role}\nNumber of Leaves : {self.No_of_leaves}\nOffice Time : {self.Office_time}")
    
harry = Employee.from_str("Harry-70,000-Instructor")
rohan = Employee.from_str("Rohan-30,000-Student")
hamad = Employee.from_str("Hamad-50,000-Assisstant Manager")


harry.access()
rohan.access()
hamad.access()


harry.change(12,"12 to 6")
print(rohan.No_of_leaves)
print(rohan.Office_time)
