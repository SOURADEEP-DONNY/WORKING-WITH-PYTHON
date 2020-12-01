n=input()
l=[]
for i in n:
    i=int(i)
    l.append(i)

s=0

for j in l:
    if j%2 != 0:
        s=s+j
print(s)
