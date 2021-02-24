'''Not using a class variable'''
class Circle:
    def __init__(self,radius,pie):
        self.radius=radius
        self.pie=pie

    def cal_cir(self):
        return 2*self.radius*self.pie

c1=Circle(10,3.14)
print(c1.cal_cir())



'''Using class variable'''
class Cir:
    pie=3.14
    def __init__(self,r):
        self.r=r

    def cal_cir(self):
        return 2*Cir.pie*self.r

c2=Cir(10)
print(c2.cal_cir())
