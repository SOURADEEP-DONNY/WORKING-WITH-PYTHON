N,K=input().split()
N=int(N)
K=int(K)
l=[]
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        if i*i==N:
            l.append(i)
        else:
            l.append(i)
            l.append(N//i)

l.sort(reverse=True)
print(l)
length=len(l)
if K>length:
    print(1,end=' ')
else:
    print(l[K-1],end=' ')
