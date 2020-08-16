
def fibo__s(N):
    num1=0
    num2=1
    if N==1:
        print(num1)
    elif N==2:
        print(num1,num2)
    else:
        print(num1,num2,end=' ')
        for i in range(N-2):
            num3=num1+num2
            num1=num2
            num2=num3
            print(num3,end=' ')

n=int(input("\nEnter total terms:-"))
fibo__s(n)
