N=int(input())
if N>=1 and N<=10**8:
    store=[]
    for i in range(1,N+1,1):
        if N%i==0:
            store.append(i)

    store.sort()
    for i in store:
        print(i,end=' ')
