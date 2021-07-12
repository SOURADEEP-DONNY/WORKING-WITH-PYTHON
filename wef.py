n=input("Enter a name:")
s=""
l=len(n)
for i in range(0,l):
    if n[i] not in s:
        s=s+n[i]
        t=n.count(n[i])
        print(n[i],t)
