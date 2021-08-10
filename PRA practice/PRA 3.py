class City:
    def __init__(self,cityId,stateName,cityName,rainfallRecieved,year):
        self.cityId=cityId
        self.stateName=stateName
        self.cityName=cityName
        self.rainfallRecieved=rainfallRecieved
        self.year=year
class RainfallAnalysis:
    def __init__(self,cityList):
        self.cityList=cityList

    def getStateWiseRainfall(self):
        l=[]
        lsta=[]
        lra=[]
        res=[]
        for i in cityList:
            if i.stateName not in l:
                l.append(i.stateName)
        for j in l:
            r=0
            for i in cityList:
                if j == i.stateName:
                    r=r+i.rainfallRecieved
                    if i.stateName not in lsta:
                        lsta.append(i.stateName)
            lra.append(r)
        res.append(lsta)
        res.append(lra)
        return res
    def findCitiesWithMoreThanAvgRainfall(self,state):
        l=[]
        l1=[]
        l2=[]
        l3=[]
        r=0
        for i in cityList:
            if i.stateName == state:
                l.append(i.cityName)
                l1.append(i.rainfallRecieved)
        
        for i in l1:
            r=r+i
        c=0
        di=dict(zip(l,l1))
        for i in l:
            c=c+1
        if c != 0:
            avg_rain=r/c
        else:
            avg_rain =0
        for i in l1:
            if avg_rain < i:
                l2.append(i)
        for i in l2:
            for j in di:
                if i==di[j]:
                    l3.append(j)
        dic=dict(zip(l3,l2))
        return dic

if __name__=='__main__':
    num=int(input())
    cityList=[]
    for i in range(num):
        cityId=int(input())
        stateName=input()
        cityName=input()
        rainfallRecieved=int(input())
        year=int(input())
        o=City(cityId,stateName,cityName,rainfallRecieved,year)
        cityList.append(o)
    obj=RainfallAnalysis(cityList)
    state=input()
    res1=obj.getStateWiseRainfall()
    res2=obj.findCitiesWithMoreThanAvgRainfall(state)
    di=dict(zip(res1[0],res1[1]))
##    for i in di:
##        print(i,di[i])
##
    l=sorted(di.items())
    if l != []:    
        for i in l:
            print(i[0],i[1])
        
    if res2:
        for i in res2:
            print(i,res2[i])
    else:
        print("No city available")
                    
