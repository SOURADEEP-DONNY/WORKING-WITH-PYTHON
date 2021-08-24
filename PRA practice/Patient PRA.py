class Patient:
    def __init__(self,code,name,age,counsellorName,billAmount):
        self.code=code
        self.name=name
        self.age=age
        self.counsellorName=counsellorName
        self.billAmount=billAmount

class Counsellor:
    def __init__(self,counsellorName,ptList):
        self.counsellorName=counsellorName
        self.ptList=ptList

    def findPatientWithMinimumAge(self):
        l=[]
        for i in ptList:
            l.append(i.age)
        min_age=min(l)
        return min_age
    def sortPatientByBillAmount(self):
        for i in ptList:
            l.append(i.billAmount)
