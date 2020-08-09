t=int(input())
if t>=1 and t<=10:
    for i in range(t):
        N=int(input())
        if N>=1 and N<=10000:
            x=[]
            count=0
            
            x=[int(i)for i in input().split()]
        
            x.insert(0,0)
            
            y=list(range(N+1))
            o_list=y


            while True:
                z=[0]*(N+1)

                for i in range(1,N+1):   #SINCE WE DON'T WANT TO ALTER THE POSITION OF 0
                    z[x[i]]=y[i]
                count=count+1
                if z==o_list:
                    print(count,end='')
                    break
                else:
                    y=z
