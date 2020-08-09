p=int(input())
if p>=1 and p<=1000000:
    t=int(input())
    if t>=1 and t<=50:
        compare=[]
        for i in range(2):
            s=int(input())
            net_amt=0
            if s>=1 and s<=30:
                for i in range(s):
                    y,rit=[float(j) for j in input().split()]
                    y=int(y)
                    #part=(1+rit)**(y*12)
                    emi=(p*(rit))/(1-1/(1+rit)**(y*12))
                    net_amt=net_amt+emi
            compare.append(emi)
    #print(compare)
    if compare[0]>compare[1]:
        print('Bank B')
    else:
        print('Bank A')
