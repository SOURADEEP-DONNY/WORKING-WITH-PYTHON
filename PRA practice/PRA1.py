class Employee:
    def __init__(self,employeeId,employeeName,gelnRole):
        self.employeeId=employeeId
        self.employeeName=employeeName
        self.gelnRole=gelnRole
        self.status="In Service"

class Organization:
    def __init__(self,employeeList):
        self.employeeList=employeeList

    def updateEmployeeStatus(self,yv):
        for i in self.employeeList:
            if i.gelnRole > yv :
                i.status="Retirement Due"
        return self.employeeList
    def countEmployees(self):
        c=0
        for i in self.employeeList:
            if i.status=="Retirement Due":
                c=c+1
        return c

if __name__=="__main__":
    c=int(input())
    employeeList=[]
    for i in range(c):
        employeeId=int(input())
        employeeName=input()
        gelnRole=int(input())
        o=Employee(employeeId,employeeName,gelnRole)
        employeeList.append(o)
    obj=Organization(employeeList)
    yv=int(input())
    res1=obj.updateEmployeeStatus(yv)
    res=obj.countEmployees()
    if res>0:
        print(res)
    else:
        print("NO UPDATE")
    for i in res1:
        print(i.employeeId,i.employeeName,i.status)
