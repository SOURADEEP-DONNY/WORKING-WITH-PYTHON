list1=[(1,3),(2,6),(5,8),(3,1)]
list2=[]
list3=[]
for i in list1:
    list2.append(i[-1])

list2.sort()
##print(list2)
for i in list2:
    for j in list1:
        if i==j[-1]:
            list3.append(j)
##print(list1)
print(list3)
