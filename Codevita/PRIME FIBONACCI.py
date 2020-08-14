#===============================FIRST LIST======================================
list1=[]
l,u=[int(i) for i in input().split()]
##u=int(input('upper '))
##l=int(input('lower '))
for i in range(l,u+1,1):
    factor=0
    for j in range(1,i+1,1):
        if i%j==0:
            factor=factor+1
    if factor==2:
        list1.append(i)
##print("List1:")
##print(list1)
#===============================================================================
temp=[]
temp=list1
list2=[]
for i in list1:
    for j in temp:
        if i != j:
            list2.append(int(str(i)+str(j)))

##print("List2:")
##print(list2,'\n\n')

res1 = []
for i in list2:
    if i not in res1:
        res1.append(i)
#==================================================================================
#===================CALCULATING PRIMES FROM 3RD LIST================================
##print('\n\nPrime for 3rd list')
list3=[]
for i in res1:
    factor=0
    for j in range(1,i+1,1):
        if i%j==0:
            factor=factor+1
    if factor==2:
        list3.append(i)
##print("List3:")
##print(list3)

res2 = []
for i in list3:
    if i not in res2:
        res2.append(i)
#======================================================================================
#=========================LENGTH OF THIRD LIST=========================================
l=len(res2)
##print("\nLength of list3=",l)

maxi=max(res2)
mini=min(res2)
#======================================================================================

#==========================Fibonacci Series=============================================
def fibo(n1,n2,length):
    if length==0:
        return
    res=n1+n2
    fibo(n2,res,length-1)
num1=maxi
num2=mini
length=l
##print(num1)
##print(num2)
fibo(num1,num2,length-2)

#========================================================================================
##num1=maxi
##num2=mini
##for i in range(l-2):
##    sumation=num1+num2
##    num1=num2
##    num2=sumation
##print(sumation,end="")
##

##print("The fibonacci is:")
num1=mini
num2=maxi
for i in range (0,l-2):
    sum=num1+num2
    num1=num2
    num2=sum

print(sum)

