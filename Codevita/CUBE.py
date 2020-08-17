import math
N=int(input())
LIST=[]
ans=0
for i in range(N):
    LIST.append(list(map(str,input().split())))
    
for j in range(N):
    for k in range(N):
        if LIST[j][k]=='D':
            ans=ans+1

res=math.floor(math.sqrt(ans))
print(res,end='')
