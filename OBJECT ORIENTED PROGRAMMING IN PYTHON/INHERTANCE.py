#=============================INHERITANCE=======================================
#===============================================================================

class base_class:
    def __init__(self,name,nickname):
        self.name=name
        self.nickname=nickname

class derived_class(base_class):
    def display(self):
        print('NAME OF THE CANDIDATE FROM BASECLASS',self.name)
        print('NICKNAME OF THE CANDIDATE FROM THE BASECLASS',self.nickname)

obj=derived_class('SOURADEEP DAS','DONNY')
obj.display()
