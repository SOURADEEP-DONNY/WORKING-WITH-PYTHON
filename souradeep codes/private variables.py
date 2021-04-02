class A:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30  #PRIVATE VARIABLE
    def public_method(self):
        print(self.__c)
        self.__private_method()  # THE PRIVATE METHOD HAS BEEN CALLED HERE
    def __private_method(self):     #PRIVATE METHOD
        print('THIS IS FROM PRIVATE METHOD')

obj=A()
print(obj.a)
print(obj._b)
obj.public_method()
