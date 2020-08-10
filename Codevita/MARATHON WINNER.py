from collections import Counter

N=int(input())
if N>1 and N<=100:
    T=int(input())
    if T>1 and T<=100:
        participant=[]
        final_dist_for_all=[]
        list2=[]

        for i in range(N):
            can=[int(i)for i in input().split()]
            unit=can[-1]
            can.pop(-1)
            s=0
            dist=[]
            for i in can:
                s=s+(i*unit)
                dist.append(s)
                #print(dist)
            final_dist_for_all.append(dist)
        print(final_dist_for_all)



        
        for i in range(T):
            list2.append(list(list(zip(*final_dist_for_all))[i]))
        print(list2)

        for i in range(1,len(list2),2):
            m=max(list2[i])
            for j in range(len(list2[i])):
                if m==list2[i][j]:
                    participant.append(j+1)

        res=dict(Counter(participant))
        values=list(res.values())
        keys=list(res.keys())

        print(keys[values.index(max(values))])
