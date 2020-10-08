# Multiple Inheritence. 


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

class Player:
    def __init__(self,name,sport,experience,status):
        self.name = name
        self.sport = sport
        self.experience = experience
        self.status = status

    @staticmethod
    def profchecker(year):
        return True if int(year) > 5 else False

    @design
    def playeraccess(self):
        print(f"Name is {self.name}.\nSport is {self.sport}.\nExperience is {self.experience} years.\nStatus is {self.status}")

karan = Player("Karan","Cricket","4","Hobby")
shubham = Player("Shubham","Tennis","11","Job")
rohan = Player("Rohan","Football","5","Hobby")

rohan.playeraccess()
karan.playeraccess()

print(Player.profchecker(karan.experience))
print(Player.profchecker(shubham.experience))
print(Player.profchecker(rohan.experience))


class CoolProgrammer(Employee,Player):
    pass

rohan = CoolProgrammer.from_str("Rohan-30,000-Student-Intern")

rohan.access()
print(rohan.Is_Intern(30000))
print(rohan.profchecker(5))
