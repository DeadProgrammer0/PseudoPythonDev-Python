# Operators Overloading and Dunder Methods.

def design(func):
    def inner(*args,**kwargs):
        print("-"*30)
        func(*args,**kwargs)
        print("-"*30)
    return inner 

class Employee:

    Place = {}

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
    
    def __add__(self,other):
        return int(self.salary) + int(other.salary)

    def __truediv__(self,other):
        return int(self.salary) / int(other.salary)

    l1 = ["Intern","Jobless"]

    def __contains__(self,other):
        return self.role in other.role

    def __str__(self):
        return f"str\nName : {self.name}\nSalary : {self.salary}\nRole : {self.role}\nNumber of Leaves : {self.No_of_leaves}\nOffice Time : {self.Office_time}\nStatus : {self.status}"

    def __repr__(self):
        return f"repr\nEmployee\n{self.name}\n{self.salary}\n{self.role}\n{self.No_of_leaves}\n{self.Office_time}\n{self.status}"

    def __bool__(self):
        return False
    
    def __ne__(self,other):
        return self.status != other.status 

    def __eq__(self,other):
        return self.Office_time == other.Office_time

    def __setitem__(self,name,place):
        self.Place[name] = place

    def __getitem__(self,item):
        return self.Place[item]

harry = Employee.from_str("Harry-55000-Programmer, Cleaner, Manager-Job")
rohan = Employee.from_str("Rohan-10000-Architect-Job")
rohan.Office_time = "12 to 8"

harry["Harry"] = "Mumbai"
rohan["Rohan"] = "Bengaluru"

print(harry + rohan) 
print(harry / rohan)
print(harry in rohan)
print(harry != rohan)
print(harry == rohan)


print(harry["Harry"])
print(rohan["Rohan"])