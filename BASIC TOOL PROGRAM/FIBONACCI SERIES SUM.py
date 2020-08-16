n1=int(input('1st NUMBER:-'))
n2=int(input('@nd NUMBER:-'))
n=int(input("\nEnter total terms:-"))
def fibo__s(first,second,N):
    num1=first
    num2=second
    s=0
    if N==1:
        s=s+num1
        print(s)
    elif N==2:
        s=s+num1+num2
        print(s)
    else:
        s=s+num1+num2
        #print(num1,num2,end=' ')
        for i in range(N-2):
            num3=num1+num2
            num1=num2
            num2=num3
            #print(num3,end=' ')
            s=s+num3
        print(s)


fibo__s(n1,n2,n)
