s1='this is my house'
s2='this is my housethis is my housethis is my housethis is my house this'
c=0
l=[]
lis=[]
lis2=[]
j=s1.split()
for p in j:
    lis.append(p)
k=s2.split()
for i in j:
    for j in k:
        if i==j:
            c=c+1
    l.append(c)
    c=0
data=dict(zip(lis,l))
print(data)
for i in data:
    if data[i]<2:
        lis2.append(i)
print(lis2)


r=lis[-1]
x=lis.index(r)
print(x)
