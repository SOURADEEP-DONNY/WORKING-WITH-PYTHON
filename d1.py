s=0
n=int(input("Enter a number: "))
while(n>0):
    q=n//10
    r=n%10
    s=s+r
    n=q
print(s)    
