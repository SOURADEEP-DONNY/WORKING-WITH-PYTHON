def arrange(N):
    if N==0:
        return 1
    elif N==1:
        return 0
    elif N==2:
        return 1
    else:
        return (N-1)*(arrange(N-1)+arrange(N-2))

N=int(input())
print(arrange(N)%1000000007)
        
