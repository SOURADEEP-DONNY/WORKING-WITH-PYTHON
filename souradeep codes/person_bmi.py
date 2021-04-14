class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight
        self.bmi=0
        self.bmi_status=""
        
    def calculatebmi(self):
        self.bmi=round(self.weight/(self.height*self.height))
        
class Society:
    def __init__(self,bmi_status,person_list):
        self.bmi_status=bmi_status
        self.person_list=person_list
        
    def calculatebmistatusbyname(self,iname):
        
        temp = False
        for person in self.person_list:
            if(person.name.lower()==iname.lower()):
                temp=True
                person.calculatebmi()
                print(person.bmi,end=" ")
                for keys in self.bmi_status.keys():
                    value = self.bmi_status[keys]
                    if(value[0]<=person.bmi and value[1]>=person.bmi):
                        person.bmi_status=keys
                        print(keys)
                    
        
        return temp
        
    def invalidpersons(self,number):
        
        invalid = []
        
        for person in self.person_list:
            person.calculatebmi()
            if(person.bmi<number):
                invalid.append(person)
                
        return invalid
        
if __name__=='__main__':        
    n = int(input())
    person_list = []
    for i in range(n):
        name = input()
        height = int(input())
        weight = int(input())
    
        person_list.append(Person(name,height,weight))
    
    bmi_status = {}
    n1 = int(input())
    for i in range(n1):
        key = input()
        l = int(input())
        u = int(input())
        if(l>u):
            l,u = u,l
        bmi_status[key] = (l,u)
    
obj = Society(bmi_status,person_list)
iname = input()
ans = obj.calculatebmistatusbyname(iname)
if(ans==False):
    print("No person Exists")
bmiv = int(input())
ans1 = obj.invalidpersons(bmiv)
for person in ans1:
    print(person.name, end = " ")
    print(person.bmi)
