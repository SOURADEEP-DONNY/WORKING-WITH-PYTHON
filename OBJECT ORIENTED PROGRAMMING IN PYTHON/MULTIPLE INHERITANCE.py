#=============================MULTIPLE INHERITANCE=======================================
#===============================================================================

class A:
    def display_A(self):
        print('this is from class A.')

class B:
    def display_B(self):
        print("THIS IS FROM CLASS B")

class C(A,B):
    pass

obj=C()
obj.display_A()
obj.display_B()
