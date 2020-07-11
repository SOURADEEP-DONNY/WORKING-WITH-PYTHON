#===============================METHOD OVERRIDING===============================
#===============================================================================

# OVERRIDING IS THE ABILITY OF THE CLASS TO CHANGE THE IMPLEMENTATION OF METHOD
# PROVIDED BY ONE OF ITS ANCESSTOR.

#===============================OR==============================================
# WE CAN CHANGE THE IMPLEMENTATION OF THE DERIVED CLASS FROM IT'S BASE CLASS.
#===============================================================================

class A:
    def display(self):
        print('\nMODIFIED BY CLASS A')

class B(A):   #INHERITATION
    def display(self):
        print('\nMODIFIED BY CLASS B')   # THIS IS METHOD OVERRIDING.

#=====================OBJECT OF CLASS A===========================================
OBJ=A()
OBJ.display()

#================================OBJECT OF CLASS B===============================
obj=B()
obj.display()
#===============================================================================
