# Diamond Shape Problem in Multiple Inheritance.
# Reference - https://media.geeksforgeeks.org/wp-content/uploads/20191222084637/Diamond1.png

class A:
    def met(self):
        print("This is Class A.")

class B(A):
    # def met(self):
    #     print("This is Class B.")
        pass

class C(A):
    # def met(self):
    #     print("This is Class C.")
    pass

class D(C,B):
    # def met(self):
    #     print("This is Class D.")
    pass

a = A()
b = B()
c = C()
d = D()

a.met()
b.met()
c.met()
d.met()
