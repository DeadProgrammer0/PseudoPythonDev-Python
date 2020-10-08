# Setters and Property Decorators.

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


harry = Employee("Hemant","Roy")
rohan = Employee("Rohan","Kumar")

rohan.explain()
print(rohan.email)

rohan.lname = "Raj"
print(rohan.email)

rohan.email = "this.that@codewithharry.com"
rohan.explain()
print(rohan.email)

del rohan.email

print(rohan.email)