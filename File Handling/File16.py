f=open("pro.txt","r")
count=0
rec=""
for i in f:
    rec=f.readline()
    if rec=="":
        break
    count = count+1
print(count,rec,end='')
print(i)
f.close()
