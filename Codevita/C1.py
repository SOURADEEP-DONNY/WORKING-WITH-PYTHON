from itertools import product
def sum__(n):
    sum=0
    for i in range(len(n)):
        sum=sum+int(n[i])
    return sum
low,high=map(int,input().split())
k=int(input())
lst_1=[]
for i in range(low,int(high**0.5)+1):
    lst_1.append(str(i))
count=0
perm=product(lst_1,repeat=k)
for i in perm:
    if (sum__(i)%2==0):
        count+=1
print(count*10)
