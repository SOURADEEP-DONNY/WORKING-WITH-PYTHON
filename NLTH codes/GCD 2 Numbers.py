def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

n1=int(input())
n2=int(input())
print(GCD(n1,n2))
