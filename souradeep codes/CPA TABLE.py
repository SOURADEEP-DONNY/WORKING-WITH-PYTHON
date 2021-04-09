class Table:
    def __init__(self,tableno,waitername,status):
        self.tableno=tableno
        self.waitername=waitername
        self.status=status
def findwaiterwisenooftables(tables):
    dic = {}
    for i in tables:
        dic[i.waitername]=0
    for i in tables:
        dic[i.waitername]+=1
    return dic
def findwaiternamebytableno(tables,number):
    for i in tables:
        if(i.tableno==number):
            return i.waitername
    return None
n = int(input())

tables = []


for i in range(n):
    tableno = int(input())
    waitername=input()
    status=input()
    b=Table(tableno,waitername,status)
    tables.append(b)
    

number=int(input())

dic = findwaiterwisenooftables(tables)

for key in sorted(dic.keys()):
    print(key+"-"+str(dic[key]))

name = findwaiternamebytableno(tables,number)

if(name==None):
    print("No waiter found")
    
else:
    print(name)
