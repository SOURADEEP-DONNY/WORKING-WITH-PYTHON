class Employee:
    def __init__(self,emp_id,emp_name,role):
        self.employeeId=emp_id
        self.employeeName=emp_name
        self.geInRole=role
        self.status="In Service"
class Organization:
    def __init__(self,emp_list):
        self.employeeList=emp_list
    def updateEmployeeStatus(self,noOfYears):
        for i in self.employeeList:
            if i.geInRole > noOfYears:
                i.status="Retirement Due"
        return self.employeeList
    def countEmployees(self):
        count=0
        for i in self.employeeList:
            if i.status=="Retirement Due":
                count+=1
        return count
if __name__=="__main__":
    num=int (input())
    emp_list=[]
    for _ in range(num):
        id=int(input())
        name=input()
        role=int(input())
        emp_list.append(Employee(id,name,role))
    obj=Organization(emp_list)
    noOfYears=int(input())
    result1=obj.updateEmployeeStatus(noOfYears)
    result2=obj.countEmployees()
    if(result2>0):
        print("Count of employee updated=",result2)
    else:
        print("No employee updated")
    for i in result1:
        print(i.employeeId,i.employeeName,i.status)
