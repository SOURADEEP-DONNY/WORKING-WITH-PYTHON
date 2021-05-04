class Table:
    def __init__(self,tableNo,waiterName,status):
        self.tableNo=tableNo
        self.waiterName=waiterName
        self.status=status

def findWaiterWiseTotalNoOfTables(tableList):
    lname=[]
    lcoun=[]
    lres=[]
    for i in tableList:
        lname.append(i.waiterName)
        lcoun.append(i.tableNo)
    l=len(lname)
    lname2=lname[::1]
    for i in range(l):
        p=lname2.pop()
        c=1
        if p in lname2:
            c=c+1
            lres.append(c)
        else:
            lres.append(c)
    lcount=lres[-1::-1]
    data=dict(zip(lname,lcount))
    return data
def findWaiterNameByTableNo(tableList,tno):
    for i in tableList:
        if tno==i.tableNo:
            return i.waiterName
    else:
        return None
if __name__=='__main__':
    n=int(input())
    tableList=[]
    for i in range(n):
        tableNo=int(input())
        waiterName=input()
        status=input()
        b=Table(tableNo,waiterName,status)
        tableList.append(b)
    tno=int(input())
    res=findWaiterWiseTotalNoOfTables(tableList)
    for i in res:
        print(i,'-',res[i])
    res1=findWaiterNameByTableNo(tableList,tno)
    if res1==None:
        print('No Waiters found')
    else:
        print(res1)
