class Container:
    def __init__(self,Id,length,breath,height,pricePerSqrFt):
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

    def findContainerCost(self,num_id):
        for i in containerList:
            if i.Id == num_id:
                return ((i.length*i.breadth*i.height)*i.pricePerSqrFt)
        else:
            return None
            

    def findLargestContainer(self):
        lvol=[]
        lres=[]
        for i in self.containerList:
            vol=i.length*i.breadth*i.height
            lvol.append(vol)
        maxi=max(lvol)
        for i in containerList:
            if maxi== ((i.length*i.breadth*i.height)):
                lres.append(i.Id)
        lres.append(maxi)
        return lres
if __name__ == '__main__':
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
    num_id=int(input())
    res=obj.findContainerCost(num_id)
    if res == None:
        print('NO CONTAINER FOUND')
    else:
        print ('cost',res)
    res=obj.findLargestContainer()
    for i in res:
        print(i,end=' ')
