# Super()

class A:

    classvar1 = "I am Class A variable."
    s = "A"

    def __init__(self):
        self.var1 = "I am in Class A constructer."
        self.classvar1 = "I am Class A instance variable."
        self.special = "A Special"


class B(A):

    classvar1 = "I am Class B variable."
    s = "B"

    def __init__(self):
        
        super().__init__()
        print(super().s) 
        self.var1 = "I am in Class B constructor."
        self.classvar1 = "I am Class B instance variable"
        self.special = "B Special"
        


a = A()
b = B()


print(a.var1)
print(a.classvar1)
print(b.var1)
print(b.classvar1)
print(b.special)