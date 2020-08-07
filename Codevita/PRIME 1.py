#========================================================================================
n=int(input())
list1=[]
for i in range(1,n+1):
    factors=0
    for j in range(1,i+1):
        if i % j == 0:
            factors=factors+1
    if factors==2:
        list1.append(i)
#######print(list1)
#  CALCULATING THE PRIME NUMBERS IN THE RANGE
##=======================================================================================
#   SUMMATION OF THE PRIME NUMBERS AND STORING IN A LIST
#========================================================================================
list2=[]
s=0
for i in list1:
    s=s+i
    list2.append(s)
######print(list2)
#========================================================================================
#  CHECKING
c=0   # final count
for i in list2:
    if i in list1 and i !=2:  #SINCE THE CODE HAS GIVEN A CONSTRAINT OF STARTING FROM 3
        ##print(i)
        c=c+1
print(c)
#========================================================================================
