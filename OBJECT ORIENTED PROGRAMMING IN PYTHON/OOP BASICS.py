#CREATING A NORMAL METHOD INSIDE A CLASS.
class testing:
    def display(self):
        print('HELLO EVERYONE!!!')

obj=testing()    # CREATING THE OBJECT OUTSIDE THE CLASS.
obj.display()    # CALLING THE METHOD WITH THE OBJECT.


#===============================================================================
print('\nFUNCTION2')
print('\n')
# ANOTHER METHOD OF INITIALISING IS THE '__init__' METHOD.

class calling:
    college='RCCIIT'   #CLASS VARIABLE
    
    #CREATING A METHOD OF INITIALISATION.
    def __init__(self,name):
        self.name=name  # INITIALISING THE NAME.
    def display(self):
        print('NAME=',self.name)  # DISPLAYING THE NAME.
        print('COLLEGE=',calling.college) # DISPLAYING A CLASS VARIABLE.

        
obj1=calling('SOURADEEP DAS')   # CREATING AN OBJECT
obj1.display()

#===============================================================================
