class A:
    def __init__(self):
        self.a=10
        self._b=100
        self.__c=1000

l=A()
print(l.a)
print(l._b)
print(l.__c)
