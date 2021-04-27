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
        for i in personList:
            s=s+i.height
        avg_height=s/(len(personList))
        return avg_height
    def findTallerThanAverage(self):
        l=[]
        for i in personList:
            avg_h=self.findAverageHeight()
            if avg_h < i.height:
                l.append(i.name)
        return l

if __name__=='__main__':
    n=int(input())
    personList=[]
    for i in range(n):
        name=input()
        height=int(input())
        weight=int(input())
        b=Person(name,height,weight)
        personList.append(b)
    obj=Society(personList)
    r1=obj.findAverageHeight()
    r2=obj.findTallerThanAverage()
    print('The average height is',r1)
    print('Person taller than avg height')
    for i in r2:
        print(i)
