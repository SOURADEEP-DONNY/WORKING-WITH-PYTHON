#=============================MULTILEVEL INHERITANCE=======================================
#===============================================================================
class grandfather:
    def display_grandfather(self):
        print("THIS IS FROM GRANDFATHER'S CLASS")

class father(grandfather):
    def display_father(self):
        print("THIS IS FROM FATHER'S CLASS")

class child(father):
    def display_child(self):
        print("THIS IS FROM CHILD'S CLASS")

obj=child()
obj.display_grandfather()
obj.display_father()
obj.display_child()

#================================================================================
        
