##class Parrot:
##    def fly(self):
##        print("Parrots can fly")
##    def swim(self):
##        print("Parrots cannot swim")
##class Penguin:
##    def fly(self):
##        print("Penguin cannot fly")
##    def swim(self):
##        print("Penguin can swim")
##
##def swimming_test(bird):
##    bird.swim()
##
##def flying_test(bird):
##    bird.fly()
##
##p=Parrot()
##pg=Penguin()
##
##p.swim()
##pg.swim()
##
##
##p.fly()
##pg.fly()
#=================================================================================
##class Car:
##    def __init__(self,speed):
##        self.__speed=speed
##    def setter(self,v):
##        self.__speed=v
##    def getter(self):
##        return self.__speed
##Safari=Car(350)
##BMW=Car(400)
##
##BMW.speed=500
##print(BMW.getter())
###========================================================================================
##from abc import ABC,abstractmethod
##class parent(ABC):
##    def f1(self):
##        pass
##    def f2(self):
##        print('Parent')
##class child(parent):
##    def f1(self):
##        print('child')
##p=child()
##p.f1()
##p.f2()
#============================================================================================
##class Test:
##    def __init__(self,x):
##        self.x=x
##    def get_data(self):
##        print('Fetch data from database')
##    def f1(self):
##        self.get_data()
##    def f2(self):
##        self.get_data()
##t=Test(8)
##def new_get_data(self):
##    print('Fetch data from test')
##Test.get_data=new_get_data
##print('After monkey patching')
##t.f1()
##t.f2()
#================================================================================================
class Person:
    def __init__(self,name):
        self.name=name
        Person.i="Static variable"
    def disp(self):
        y="Local variale"
        print(y)
        print(self.name)
        print(Person.i)
obj=Person('Soura')
obj.disp()











