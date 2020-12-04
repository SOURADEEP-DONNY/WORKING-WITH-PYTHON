f=open("aaa.txt","r")
o=f.read()
l=len(o)
temp=""
u=0
while u<l:
    if o[u] not in temp:
        temp=temp+o[u]
        t=o.count(o[u])
        print(o[u],':',t)
        u=u+1
    
