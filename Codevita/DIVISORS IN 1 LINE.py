N=int(input())
if N>=1 and N<=10**8:
    store=[]
    for i in range(1,N+1,1):
        if N%i==0:
            store.append(i)

    store.sort()
    for i in store:
        print(i,end=' ')


print('\n\n')
# THE ABOVE CODE WILL NOT RUN IN ANY COMPETITIVE EXAM AND WILL GIVE A RUNTIME
# ERROR.

N=int(input())
if N>=1 and N<=10**8:
    store=[]

    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            if i*i==N:
                store.append(i)
            else:
                store.append(i)
                store.append(N//i)

        store.sort()
    for i in store:
        print(i,end=' ')


print('\n\n')


# ANOTHER SLOTUION
N=int(input())
store=[]
if N>=1 and N<=10**8:
   

    for i in range(1,int(N**0.5)+1):
        if N%i==0:
            if i*i==N:
                print(i,end=' ')
            else:
                print(i,end=' ')
                store.insert(0,N//i)
    for i in store:
        print(i,end=' ')
