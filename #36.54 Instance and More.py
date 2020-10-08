# Instance and Class Variable.

class Employee:
    # These are Class variables that belongs to all the Objects in the Class.
    No_of_leaves = 10
    Office_Time = "9 to 5"
    pass

# Here we created two Object in Employee Class.
harry = Employee()
rohan = Employee()

# These are some Instance variable that belongs to their specific Object.

harry.name = "Harry"
harry.salary = 70000
harry.role = "Instructer"


rohan.name = "Rohan"
rohan.salary = 30000 
rohan.role = "Student"



print(harry.name)
print(rohan.role)
print(harry.No_of_leaves)
print(rohan.Office_Time)

# Changing Class variables.
# You can change Class variable directly to implement changes for all Objects in Class.

print("\nChanged")

Employee.No_of_leaves -= 2
print("Harry",harry.No_of_leaves)
print("Rohan",rohan.No_of_leaves)

# Changing Class variable for a specific Object.
# You can change the Class variable for a specific object as shown below.
# But the command given below doesn't really changes the class variable It assigns a new Instance variable for the give Object.(here Rohan)

print("\nChanged for Rohan")

rohan.Office_Time = "12 to 6"
print("Rohan",rohan.Office_Time)
print("Harry",harry.Office_Time)

# Getting all the Class variables and Instance variables in form of Dict using __dict__ attribute.

# Getting Dict of Class variables.
print(Employee.__dict__)

# Getting Dict of Instance variables.
print(harry.__dict__)
print(rohan.__dict__)