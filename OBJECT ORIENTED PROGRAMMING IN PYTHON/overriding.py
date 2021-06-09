class A:
    def show(self):
        print('From class A')
class B(A):
    def show(self):
        print('Overriding and showing From class B')

b=B()
b.show()
