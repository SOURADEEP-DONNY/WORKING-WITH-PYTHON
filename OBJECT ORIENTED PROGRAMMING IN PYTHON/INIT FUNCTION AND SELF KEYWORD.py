#CREATING A CLASS AND USING init & self KEYWORD.

class IDS:
    def __init__(self,name,department,fav_sport):
        print('The init is called')
        print(name)
        print('\n')
        self.name=name
        self.department=department
        self.fav_sport=fav_sport

diploma=IDS('Sujatro Ghosh','ECE','FOOTBALL')
btech=IDS('Souradeep Das','ECE','TABLE TENNIS')
mtech=IDS('Arjun Das','CSE','CRICKET')
phd=IDS('Deepsha Das','CSE','TENNIS')

print('NAME OF THE M.TECH STUDENT IS',mtech.name)
print('NAME OF THE B.TECH STUDENT IS',btech.name)
