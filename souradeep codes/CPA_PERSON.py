class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

class Society:
    def __init__(self,personList):
        self.personList=personList

    def findAverageHeight(self):
        l=[]
        for i in self.personList:
            l.append(i.height)
        return sum(l)/len(l)

    def findTallerThanAveragePerson(self):
        l=[]
        average=self.findAverageHeight()
        for i in self.personList:
            if (average<i.height):
                l.append(i.name)
        return l
if __name__=='__main__':
    num=int(input())
    personList=[]
    for i in range(num):
        name=input()
        height=int(input())
        weight=int(input())
        personList.append(Person(name,height,weight))
    obj=Society(personList)
    r1=obj.findAverageHeight()
    r2=obj.findTallerThanAveragePerson()
    print('AVERAGE HEIGHT = ',r1)
    for i in r2:
        print(i)
