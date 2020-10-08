# Abstract Base Class and @abstractmethod

from abc import ABC, abstractmethod

class Shapes(ABC):
    @abstractmethod
    def printarea(self):
        return 0
        
class square(Shapes):

    name = "Square"
    sides = "4"
    
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def printarea(self):
        return self.length * self.breadth

class rectangle(square,Shapes):
    name = "Rectangle"

class parallelogram(square,Shapes):
    name = "Parallelogram "

sq1 = square(8,8)
sq2 = square(21,21)

print(sq1.printarea())
print(sq2.printarea())

rec1 = rectangle(10,6)
rec2 = rectangle(25,11)

print(rec1.printarea())
print(rec2.printarea())

par1 = parallelogram(20,10)
par2 = parallelogram(30,15)

print(par1.printarea())
print(par2.printarea())