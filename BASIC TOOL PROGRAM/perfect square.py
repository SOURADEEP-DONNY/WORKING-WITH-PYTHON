n=int(input())
for i in range(1,n+1,1):
    sq=i*i
    if sq<n or sq==n:
        if sq==n:
            print(n,'yes')
            break
else:
    print(n,'no')
