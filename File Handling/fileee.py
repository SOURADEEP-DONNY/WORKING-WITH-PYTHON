f=open("Abhi.txt","r")
s=f.read()
p=0
l=[]
for i in s:
    if(i.isdigit()):
        l.append(i)
        for j in l:
            z=int(j)
            p=p+z
print(p)        
