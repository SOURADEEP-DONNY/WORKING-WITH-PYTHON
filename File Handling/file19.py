f=open("pro.txt","r")
count=0
r=f.readline()
c=r.split("\n")
for i in c:
    t=i.strip()
    if i in c:
        count=count+1
print(count)
