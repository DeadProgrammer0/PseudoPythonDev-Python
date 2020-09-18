# Functions

# Built-in Functions
# Built-in Functions are Pre-defined.


a = 5
b = 6
c = sum((a,b))
d = max((a,b))

print(c,"\n",d)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
seasons.reverse()
list(enumerate(seasons))
print(seasons)


# User-Defined Functions.
# User Functions are defined by users.

def Average(a,b): #Functions can take inputs but its not neccessary all the times.
    """This Function can only handle 2 numbers.""" #First String of the Function is determined as Docstring.
    average = (a+b)/2
    return average #Returns the given argument else returns None (here its average).

print(Average(14,60))
print(Average.__doc__)



def Table(a):
    """Prints the Table of the given Digit."""
    inc = 1
    while(1):
    
        if inc <= 10:
            
            print(f"{a} * {inc} =",a*inc)
            inc = inc + 1
            continue

        if inc > 10:
            break 

    return "Here is your Table."
      
print(Table.__doc__)      
print(Table(9))
