f=open("Abhi.txt","r")
s=f.read()
count=0
for v in s:
    if(v=='a' or v=='e' or v=='i' or v=='o' or v=='u'):
        count=count+1
print(count)        
