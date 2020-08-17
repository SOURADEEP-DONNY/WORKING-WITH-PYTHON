import math
N=int(input())
l_1=[]
c1=0
for i in range(N):
    l_1.append(list(map(str,input().split())))
for j in range(N):
    for k in range(N):
        if l_1[j][k]=='D':
            c1+=1

print(math.floor(math.sqrt(c1)))
