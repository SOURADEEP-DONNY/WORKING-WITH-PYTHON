class Employee:
    def __init__(self,employee_name,designation,salary,leaveBalance):
        self.employee_name=employee_name
        self.designation=designation
        self.salary=salary
        self.leaveBalance=leaveBalance

class Organization:
    def __init__(self,employee_list):
        self.employee_list=employee_list

    def checkLeaveEligibility(self,name,ltype,days):
        for i in employee_list:
            if i.employee_name==name:
                for p in i.leaveBalance:
                    if p == ltype.upper():
                        if i.leaveBalance[p] > days:
                            i.leaveBalance[p]=i.leaveBalance[p]-days
                            return i.leaveBalance
        return False
if __name__=="__main__":
    num=int(input())
    employee_list=[]
    for i in range(num):
        employee_name=input()
        designation=input()
        salary=int(input())
        ch=int(input())
        t=[]
        l=[]
        for i in range(ch):
            t.append(input())
            l.append(int(input()))
        leaveBalance=dict(zip(t,l))
        o=Employee(employee_name,designation,salary,leaveBalance)
        employee_list.append(o)
    obj=Organization(employee_list)
    name=input()
    ltype=input()
    days=int(input())
    res=obj.checkLeaveEligibility(name,ltype,days)
    if res:
        print('leave granted')
        for i in res:
            print(i,':',res[i])
    else:
        print('leave not granted')
        print('Employee not found')
        
