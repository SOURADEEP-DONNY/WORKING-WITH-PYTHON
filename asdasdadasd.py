f=open("Abhi.txt","r")
s=f.read()
p=0
l=[]
for i in s:
    if(i.isdigit()):
        s=l[i]
        print(s)
        
#        for j in s:
#            j=int(j)
#            p=p+j
#print(p)        
