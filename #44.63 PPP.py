# Public , Protected and Private.

# Public - The members of a class that are declared public are easily accessible from any part of the program.
# All data members and member functions of a class are public by default.

# Protected - The members of a class that are declared protected are only accessible to a class derived from it.
# Data members of a class are declared protected by adding a single underscore ‘_’ symbol before the data member of that class.

# Private - The members of a class that are declared private are accessible within the class only, private access modifier is the most secure access modifier.
# Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.

def design(func1):
    def inner(*args,**kwargs):
        print("*"*30)
        func1(*args,*kwargs)
        print("*"*30)
    return inner


def design2(func1):
    def inner(*args,**kwargs):
        print("#"*30)
        func1(*args,*kwargs)
        print("#"*30)
    return inner

class Students:
    

    School = "Random School"

    @staticmethod
    def fee_paid_check(fee):
        return True if fee == "Paid" else False
    

    @classmethod
    def ez(cls,string):
        return cls(*string.split("/"))

    def __init__(self,name,std,sec,roll,fee):
        self._name = name
        self.__std = std
        self.__sec = sec
        self.__roll = roll
        self._fee = fee

    
    @design2
    def private(self):
        print(f"Std : {self.__std}",
        f"\nSec : {self.__sec}",
        f"\nRoll No. : {self.__roll}")


    @design
    def details_st(self):
        print(f"Name : {self._name}",
        f"\nStd : {self.__std}",
        f"\nSec : {self.__sec}",
        f"\nRoll No. : {self.__roll}",
        f"\nFee : {self._fee}")

aman = Students.ez("Aman/8/B/26/Paid")
rohan = Students.ez("Rohan/8/C/21/Paid")
harry = Students.ez("Harry/8/C/6/Dues")

aman.details_st()
rohan.details_st()
harry.details_st()

print(Students.School)
print(rohan._name)
print(harry._Students__roll)


class Exam(Students):

    @staticmethod
    def cangive_exam(func):
        return f"Yes, can give Exams." if func == True else f"No, can't give Exams."

print(Exam.cangive_exam(Students.fee_paid_check(rohan._fee)))






