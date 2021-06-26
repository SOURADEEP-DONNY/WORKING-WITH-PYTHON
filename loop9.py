pp=0
nn=0
s=0
for i in range(1,11):
    n=int(input("Enter numbers: "))
    if(n>0):
        pp=pp+1
    else:
        nn=nn+1
    s=s+n
else:
    avg=s/10
print(avg)
print(pp)
print(nn)
    
