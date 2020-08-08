t=int(input())
if t>=1 and t<=10:
    for i in range(t):
        N=int(input())
        if N>=1 and N<=10000:
            c=[]
            k=input("\nInput No. of Chocolates space separated:-")
            for i in k:
                if i != ' ':
                    i=int(i)
                    c.append(i)
            c.sort()
            time=[]
            final_result=0
            while(len(c)>=2):
                c.sort()
                sum1=c[0]+c[1]
                c.pop(0)
                c.pop(0)
                c.append(sum1)
                c.sort()
                time.append(sum1)
        final_result=sum(time)
        print(final_result)
        
