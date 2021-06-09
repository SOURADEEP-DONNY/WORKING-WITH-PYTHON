l=[]
l2=[]
m=int(input())
n=int(input())
for i in range(m):
    for i in range(n):
        l.append(int(input()))
    l2.append(l)
    l=[]
for i in l2:
    print(i)
