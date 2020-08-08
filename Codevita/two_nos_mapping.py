list1=[1,22,3,301]
temp=[]
list2=[]
temp=list1
for i in list1:
    for j in temp:
        if i != j:
            list2.append(int(str(i)+str(j)))

print(list2)
