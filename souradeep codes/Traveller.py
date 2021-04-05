class Traveler:
    def __init__(self,travelerName,traveledCountry,travelerAge,countryFrom):
        self.travelerName=travelerName
        self.traveledCountry=traveledCountry
        self.travelerAge=travelerAge
        self.countryFrom=countryFrom

class TravelAgency:
    def __init__(self,travelerList):
        self.travelerList=travelerList

    def countTravelersTraveledCountry(self,coun_name):
        count=0
        for i in travelerList:
            for j in i.traveledCountry:
                if j == coun_name:
                    count=count+1
        return count

    def getTravelerTraveledMaxCountry(self):
        max1=0
        name=''
        for i in travelerList:
            if(len(i.traveledCountry)>max1):
                max1=len(i.traveledCountry)
                name=i.travelerName
        return name

if __name__=='__main__':
    n=int(input())
    travelerList=[]
    for i in range(n):
        travelerName=input()
        traveledCountry=[]
        tot=int(input())
        for i in range(tot):
            traveledCountry.append(input())
        travelerAge=int(input())
        countryFrom=input()
        b=Traveler(travelerName,traveledCountry,travelerAge,countryFrom)
        travelerList.append(b)
    obj=TravelAgency(travelerList)
    coun_name=input()
    res=obj.countTravelersTraveledCountry(coun_name)
    print(res)
    res=obj.getTravelerTraveledMaxCountry()
    print(res)
            
