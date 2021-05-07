class Boutique:
    def __init__(self,boutiqueid,boutiquename,boutiquetype,boutiquerating,points):
        self.boutiqueid=boutiqueid
        self.boutiquename=boutiquename
        self.boutiquetype=boutiquetype
        self.boutiquerating=boutiquerating
        self.points=points

class OnlineBoutique:
    def __init__(self,boutiqueDict):
        self.boutiqueDict=boutiqueDict

    def getboutique(self,flow,fupp,eptr,strv):
        l2=[]
        c1=0
        c2=0
        for i in boutiqueDict:
            if i.boutiquetype == strv:
                c1=c1+1
                if i.boutiquerating >= flow and i.boutiquerating <= fupp:
                    c2=c2+1
                    l=[]
                    i.points=i.points+eptr
                    l.append(i.boutiqueid)
                    l.append(i.boutiquename)
                    l.append(i.points)
                    l2.append(l)
        return l2
if __name__=='__main__':
    n=int(input())
    boutiqueDict=[]
    for i in range(n):
        boutiqueid=int(input())
        boutiquename=input()
        boutiquetype=input()
        boutiquerating=float(input())
        points=int(input())
        b=Boutique(boutiqueid,boutiquename,boutiquetype,boutiquerating,points)
        boutiqueDict.append(b)
    obj=OnlineBoutique(boutiqueDict)
    flow=float(input())
    fupp=float(input())
    eptr=int(input())
    strv=input()
    res=obj.getboutique(flow,fupp,eptr,strv)
    if res==None:
        print('No botique found')
    else:
        for i in res:
            for j in i:
                print(j, end=' ')
            print('\n')
    
    
