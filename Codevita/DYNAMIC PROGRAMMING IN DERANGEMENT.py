def dynamic_counter(N):
    list_for_derangement=[0 for i in range(N+1)]

    #PROVIDING BASE CONDITIONS
    list_for_derangement[0]=1
    list_for_derangement[1]=0
    list_for_derangement[2]=1

    for i in range(3,N+1,1):
        list_for_derangement[i]=(i-1)*(list_for_derangement[i-1]+list_for_derangement[i-2])
    return list_for_derangement[N]

N=int(input())
print(dynamic_counter(N)%1000000007)
        
