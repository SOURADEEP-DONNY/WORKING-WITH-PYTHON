ld=0
fd=0
s=0
n=int(input("Enter a number: "))
ld=n%10
while(n>0):
    q=n//10
    r=n%10
    fd=r
    n=q
s=ld+fd
print(s)
