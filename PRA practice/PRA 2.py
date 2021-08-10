class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

class Society:
    def __init__(self,personList):
        self.personList=personList

    def findAverageHeight(self):
        s=0
        c=0
        for i in personList:
            s=s+i.height
            c=c+1
        avg_h=s/c
        return avg_h
    def findTallerThanAveragePerson(self):
        l=[]
        s=0
        c=0
        for i in personList:
            s=s+i.height
            c=c+1
        avg_h=s/c
        for i in personList:
            if i.height > avg_h:
                l.append(i.name)
        return l

if __name__=='__main__':
    n=int(input())
    personList=[]
    for i in range(n):
        name=input()
        height=int(input())
        weight=int(input())
        o=Person(name,height,weight)
        personList.append(o)
    obj=Society(personList)
    res=obj.findAverageHeight()
    print('The average height is ',res)
    res2=obj.findTallerThanAveragePerson()
    print('Persons taller than the Average height')
    for i in res2:
        print(i)
