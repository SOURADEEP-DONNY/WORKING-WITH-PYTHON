class Blood:
    def __init__(self,bloodGroup,unitInHand):
        self.bloodGroup=bloodGroup
        self.unitInHand=unitInHand

class BloodBank:
    def __init__(self,bloodList):
        self.bloodList=bloodList

    def isBloodAvailable(self,bg,ur):
        for i in bloodList:
            if bg == i.bloodGroup:
                if ur <= i.unitInHand:
                    return True
                else:
                    return False
        else:
            return False

    def findMinBloodStock(self):
        l=[]
        l2=[]
        res=[]
        for i in bloodList:
            l.append(i.bloodGroup)
            l2.append(i.unitInHand)
        data=dict(zip(l,l2))
        mini=min(l2)
        for i in data:
            if mini==data[i]:
                res.append(i)
        return res
if __name__=='__main__':
    n=int(input())
    bloodList=[]
    for i in range(n):
        bloodGroup=input()
        bloodGroup=bloodGroup.upper()
        unitInHand=int(input())
        b=Blood(bloodGroup,unitInHand)
        bloodList.append(b)
    obj=BloodBank(bloodList)
    bg=input()
    bg=bg.upper()
    ur=int(input())
    res=obj.isBloodAvailable(bg,ur)
    if res==False:
        print('Blood is not Available')
    else:
        print('Blood is Available')
    r=obj.findMinBloodStock()
    for i in r:
        print(i)
