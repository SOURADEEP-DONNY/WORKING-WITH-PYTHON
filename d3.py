max=0
min=9
n=int(input("Enter a number: "))
while(n>0):
    q=n//10
    r=n%10
    if(max<r):
        max=r
    if(min>r):
        min=r
    n=q    
print(max)
print(min)
