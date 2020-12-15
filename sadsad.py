f=open("Abhi.txt","r")
q=f.read()
d=q.split()
count=0
for i in d:
    if(i[-1]=='d'):
        count=count+1
        print(count)
        
