def check_prime(n):
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False

nums=[1,2,3,4,5,6,7,8,9]
prime_list=[]
for i in nums:
    p=check_prime(i)
    if p==True:
        prime_list.append(i)

print(prime_list)
