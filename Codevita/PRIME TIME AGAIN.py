D,P=input().split()
D=int(D)
P=int(P)
duration=D//P
list1=[i for i in range(2,D+1,1)]
def check_prime(n):
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False

prime_list=[]
for i in list1:
    p=check_prime(i)
    if p==True:
        prime_list.append(i)
#print(prime_list)
list2=[]
list3=[]


for i in prime_list:
    for z in range(0,P,1):
        k=duration*z
        if i+k in prime_list:
            list2.append(i+k)
    list3.append(list2)
    list2=[]

#print(list3)

count=0
for f in list3:
    if len(f)==P:
        count=count+1
print(count)
