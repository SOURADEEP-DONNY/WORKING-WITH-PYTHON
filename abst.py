from abc import ABC, abstractmethod
class parent(ABC):
    @abstractmethod
    def fun1(self):
        pass
    def fun2(self):
        print('This is a parent class')
class child(parent):
    def fun1(self):
        print('Child class')
obj=child()
obj.fun1()
obj.fun2()
