class Container:
    def __init__(self,Id,length,breadth,height,pricePerSqrFt):
        self.Id=Id
        self.length=length
        self.breadth=breadth
        self.height=height
        self.pricePerSqrFt=pricePerSqrFt
    def findVolume(self):
        return (self.length*self.breadth*self.height)

class PackagingCompany:
    def __init__(self,containerList):
        self.containerList=containerList

    def findContainerCost(self,nid):
        for i in containerList:
            if i.Id == nid:
                cost=((i.length*i.breadth*i.height)*i.pricePerSqrFt)
                return cost
        return None

    def findLongestContainer(self):
        l=[]
        l2=[]
        res=[]
        for i in containerList:
            vol=i.length*i.breadth*i.height
            l.append(vol)
            l2.append(i.Id)
        data=dict(zip(l2,l))
        maxi=max(l)
        for i in data:
            if maxi==data[i]:
                res.append(i)
                res.append(data[i])
        return res
if __name__=='__main__':
    n=int(input())
    containerList=[]
    for i in range(n):
        Id=int(input())
        length=int(input())
        breadth=int(input())
        height=int(input())
        pricePerSqrFt=int(input())
        b=Container(Id,length,breadth,height,pricePerSqrFt)
        containerList.append(b)
    obj=PackagingCompany(containerList)
    nid=int(input())
    r=obj.findContainerCost(nid)
    if r==None:
        print('Container Not Found')
    else:
        print(r)
    r=obj.findLongestContainer()
    for i in r:
        print(i,end=' ')
