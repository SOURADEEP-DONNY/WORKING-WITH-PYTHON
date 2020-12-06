f=open("Abhi.txt","r")
s=f.readline()
count=0
for v in f:
    if(v=='a' or v=='e' or v=='i' or v=='o' or v=='u'):
        count=count+1
print(count)        
        
