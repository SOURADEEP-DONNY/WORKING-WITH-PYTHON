class Employee:
    def __init__(self,employeeId,employeeName,department,salary,role):
        self.employeeId=employeeId
        self.employeeName=employeeName
        self.department=department
        self.salary=salary
        self.role=role

    def calculateincentive(self,roleIncentivePercentage):
        lin=[]
        c=0
        for i in empList:
            for j in roleIncentivePercentage:
                inc=0
                if i.role==j:
                    c=c+1
                    inc=i.salary*(roleIncentivePercentage/100)
                    lin.append(inc)
        if c==0:
            return None
        else:
            return lin

def calculateEmployeeSalaryByRole(rol,empList,roleIncentivePercentage):
    p=0
    l2=[]
    for i in empList:
        for k in roleIncentivePercentage:
            if i.role==rol and k==rol:
                p=p+1
                l=[]
                l.append(i.employeeId)
                l.append(i.employeeName)
                i.salary=i.salary+(i.salary*(roleIncentivePercentage[k]/100))
                l.append(i.salary)
                l2.append(l)
    if p==0:
        return None
    else:
        return l2

if __name__=='__main__':
    n=int(input())
    lr=[]
    lp=[]
    for i in range(n):
        r=input()
        p=int(input())
        lr.append(r)
        lp.append(p)
    roleIncentivePercentage=dict(zip(lr,lp))
    num=int(input())
    empList=[]
    for i in range(num):
        employeeId=int(input())
        employeeName=input()
        department=input()
        salary=int(input())
        role=input()
        b=Employee(employeeId,employeeName,department,salary,role)
        empList.append(b)
    rol=input()
    res=calculateEmployeeSalaryByRole(rol,empList,roleIncentivePercentage)
    if res==None:
        print('Employee Not Found')
    else:
        for i in res:
            for j in i:
                print(j,end=' ')
            print()
