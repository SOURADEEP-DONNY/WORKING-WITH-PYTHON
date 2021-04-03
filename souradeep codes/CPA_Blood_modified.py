class Blood:
    def __init__(self,bloodGroup,unitInHand):
        self.bloodGroup=bloodGroup
        self.unitInHand=unitInHand

class BloodBank:
    def __init__(self,bloodList):
        self.bloodList=bloodList

    def isBloodAvailable(self,bgroup,unit):    
        for i in self.bloodList:
            if i.bloodGroup == bgroup:
                if i.unitInHand>=unit:
                    return True
        else:
            return False

    def findMinBloodStock(self):
        mini=self.bloodList[0].unitInHand
        bglist=[]
        for i in self.bloodList:
            if(mini>i.unitInHand):
                mini=i.unitInHand
        for i in self.bloodList:
            if(mini==i.unitInHand):
                bglist.append(i.bloodGroup)
        return bglist

if __name__=='__main__':
    n=int(input())
    bloodList=[]
    for i in range(n):
        bloodGroup=input()
        unitInHand=int(input())
        b=Blood(bloodGroup,unitInHand)
        bloodList.append(b)
    obj=BloodBank(bloodList)
    bgroup=input()
    unit=int(input())
    res=obj.isBloodAvailable(bgroup,unit)
    if res==True:
        print('Blood Available')
    else:
        print('Blood Not Available')
    res=obj.findMinBloodStock()
    for i in res:
        print(i)
            
