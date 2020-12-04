f=open("Mo.txt","w")
f.write("Name""   ""Roll""    ""ComputerScience Marks")
name=""
l=[]
l_name=[]
maxi=0
for i in range(3):
    r=input("Enter Name: ")
    l_name.append(r)
    n=input("Enter Roll: ")
    c=int(input("Enter ComputerScience: "))
    l.append(c)
le=len(l)
print(l)
print(l_name)
maxi=max(l)
#print(maxi)
for i in range(0,le,1):
    if maxi in l:
        name=l_name[i]
print(name)

            
        

    
