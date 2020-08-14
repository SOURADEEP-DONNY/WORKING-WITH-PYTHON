n=int(input())
prime=[]
for i in range(1,n+1,1):
    factors=0
    for j in range(1,i+1,1):
        if i%j==0:
            factors=factors+1
    if factors==2:
        prime.append(i)

#print(prime)

count=0
for z in range(1,len(prime)):
    sum1=0
    for y in prime:
        sum1=sum1+y
        if sum1==prime[z]:
            count=count+1
        if sum1>prime[z]:
            break
print(count)
