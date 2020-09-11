n=input("\nEnter a number")
ad=0
list1=[]
for i in n:
    list1.append(i)
k=list1[-1]
k=int(k)

for i in list1:
    i=int(i)
    ad=ad+(i**k)
    

##print(ad)
n=int(n)
if ad==n:
    print(True)
else:
    print(False)
    
