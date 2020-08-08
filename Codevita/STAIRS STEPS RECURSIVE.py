def Find_ways(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    else:
        return Find_ways(n-3)+Find_ways(n-2)+Find_ways(n-1)

n=int(input())
print(Find_ways(n))
