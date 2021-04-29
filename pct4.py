class Traveller:
    def __init__(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName=travelerName
        self.traveledCountry=traveledCountry
        self.travelerAge=travelerAge
        self.countryFrom=countryFrom

class TravelAgency:
    def __init__(self,travelerList):
        self.travelerList=travelerList

    def countTravelerTraveledCountry(self,cname):
        c=0
        for i in travelerList:
            for j in i.traveledCountry:
                if j==cname:
                    c=c+1
        return c

    def getTravellerTravelledMaxCountry(self):
        tlistlen=[]
        travlist=[]
        res=[]
        for i in travelerList:
            tlistlen.append(len(i.traveledCountry))
            travlist.append(i.travelerName)
        maxi=max(tlistlen)
        data=dict(zip(travlist,tlistlen))
        for i in data:
            if maxi== data[i]:
                res.append(i)
        return res

if __name__ == '__main__':
    n=int(input())
    travelerList=[]
    for i in range(n):
        travelerName=input()
        traveledCountry=[]
        ch=int(input())
        for i in range(ch):
            cc=input()
            traveledCountry.append(cc)
        travelerAge=int(input())
        countryFrom=input()
        b=Traveller(travelerName,traveledCountry,travelerAge,countryFrom)
        travelerList.append(b)
    obj=TravelAgency(travelerList)
    cname=input()
    r=obj.countTravelerTraveledCountry(cname)
    print(r)
    r2=obj.getTravellerTravelledMaxCountry()
    for i in r2:
        print(i)
