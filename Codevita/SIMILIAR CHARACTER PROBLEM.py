N=int(input())
if N>=1 and N<=500000:
    S=[i for i in input()]
    C=[]
    S1=[]
    Q=int(input())
    if Q>=1 and Q<=10000:

        for i in range(Q):
            P=int(input())
            k=''
            count=0
            k=S[P-1]
            S1 = S[:P-1]
            for i in S1:
                if i==k:
                    count=count+1
            C.append(count)
        for i in C:
            print(i)
