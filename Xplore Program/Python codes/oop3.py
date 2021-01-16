class Student:
    def __init__(self,first_name,last_name,age):
        self.first=first_name
        self.last=last_name
        self.age=age

    def age_cal(self):
        if self.age>=60:
            return "Seniour Citizen"
        else:
            return "Minor"

'''Creating objects'''
obj1=Student('Souradeep','Das',23)
obj2=Student('Rabin','Das',82)

print(obj1.age_cal())
print(obj2.age_cal())

'''Can also be called as'''
print(Student.age_cal(obj1))
print(Student.age_cal(obj2))
