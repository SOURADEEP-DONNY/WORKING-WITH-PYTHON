#-----------------------------SPECIAL FACTOR CODE-----------------------------------
#--------------------------------------------------------------------------------
else_part=1
N=int(input('\nENTER A NUMBER:-'))
lst=[]
i=1
for i in range(1,N+1,1):
    i=int(i)
    if N%i == 0:
        lst.append(i)

lst_new=lst[-1::-1]
print(lst_new)
l=len(lst_new)
K=int(input('\nEnter the largest factor:-'))
if K<=l:
    print(lst_new[K-1])
else:
    print(else_part)

#================================================================================
