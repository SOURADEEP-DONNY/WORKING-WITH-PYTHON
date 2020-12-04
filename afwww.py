f=open("Abhi.txt","r")
q=f.readlines()
c=0
for i in q:
    if(i[1]=="a"):
        c=c+1
        print(i,end="")
print("\n",c)        
