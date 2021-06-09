class Student:
    school="RCCIIT"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def clss_method(cls):
        return cls.school

    @staticmethod
    def static_method():
        return("This is a static method")

s1=Student(10,20,30)
s2=Student(15,25,8)
print(s1.avg())
print(s2.avg())

print(Student.clss_method())

print(Student.static_method())

