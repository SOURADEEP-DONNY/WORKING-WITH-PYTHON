n=input("Enter a name: ")
i=0
l=len(n)
t2=""
while i<l:
    if n[i] not in t2:
        t2=t2+n[i]
        t=n.count(n[i])
        i=i+1
        print(n[i],t)
