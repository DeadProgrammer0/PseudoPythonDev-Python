# Single Inheritance.


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


    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))

    
    @staticmethod
    def Is_Intern(salary):
        return True if int(salary) < 30001 else False

    def __init__(self,name,salary,role,status):
        self.name = name
        self.salary = salary
        self.role = role
        self.status = status

    @design    
    def access(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nRole : {self.role}\nNumber of Leaves : {self.No_of_leaves}\nOffice Time : {self.Office_time}\nStatus : {self.status}")
    
harry = Employee.from_str("Harry-70,000-Instructor-Job")
rohan = Employee.from_str("Rohan-30,000-Student-Intern")
hamad = Employee.from_str("Hamad-50,000-Assisstant Manager-Job")


harry.access()
rohan.access()
hamad.access()


inp = input("Enter Salary here : ")

print(Employee.Is_Intern(inp))

# Single Inheritance.

class Programmer(Employee):
    def __init__(self,name,salary,role,status,languages):
        self.name = name
        self.salary = salary
        self.role = role
        self.status = status
        self.languages = languages

    @design
    def progaccess(self):
        print(f"Name is {self.name}.\nSalary is {self.salary}.\nRole is {self.role}.\nStatus is {self.status}.\nLanguages are {self.languages}.")

shubham = Programmer.from_str("Shubham-60,000-Programmer-Intern-Python, C++, Java")

shubham.progaccess()

print(shubham.No_of_leaves)