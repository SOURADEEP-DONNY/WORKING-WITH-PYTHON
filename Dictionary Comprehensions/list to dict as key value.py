a='adidas'
k=[]
v=[]
for i in a:
    k.append(i)
ke=k[::1]
l=len(k)
for i in range(l):
    p=k.pop()
    c=1
    if p in k:
        c=c+1
        v.append(c)
    else:
        v.append(c)
val=v[-1::-1]
data=dict(zip(ke,val))
print(data)
