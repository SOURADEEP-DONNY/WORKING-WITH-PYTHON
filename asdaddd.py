f=open("Abhi.txt","r")
s=f.read()
c=0
for i in s:
    if(i.isdigit()):
        c=c+1
print(c)
        
        
