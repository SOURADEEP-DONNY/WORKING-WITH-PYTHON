t=int(input())
if t>=1 and t<=1000:
    def hcf(x,y):
        if y==0:
            return x
        return hcf(y,x%y)

    store=[]
    for i in range(t):
        n1,n2=[int(i) for i in input().split()]
        r=hcf(n1,n2)
        store.append(r)

    for i in store:
        print(i)
            
