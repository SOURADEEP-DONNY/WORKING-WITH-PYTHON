D={}
p=int(input())
q=int(input())
r=int(input())
s=int(input())

ans=0

for i in range(p,q+1):
    for j in range(r,s+1):
        ans=ans+count(i,j)


print(ans)

def count(a,b):
    minimum=min(a,b)
    maximum=min(a,b)

    i=(minimum,maximum)
    if i in D:
        return D[i]

    if minimum==0:
        return 0
    if minimum==1:
        return a*b

    chocolate=maximum//minimum
    new_side=maximum%minimum
    chocoloate=chocolate+count(new_side,minimum)

    D[i]=chocolate
    return chocolate
