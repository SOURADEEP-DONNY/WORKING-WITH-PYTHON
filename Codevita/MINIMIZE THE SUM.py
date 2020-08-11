N,K=[int(i)for i in input().split()]
if N>=1 and N<=10**5:
    if K>=1 and K<=10**5:
        list1=[int(i)for i in input().split()]
        for i in range(K):
            m=max(list1)
            ind=list1.index(m)
            list1.pop(ind)
            m=m//2
            list1.insert(ind,m)
            #print(list1)

        tot=0
        for j in list1:
            tot=tot+j
        print(tot)
        
        
