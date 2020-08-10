list1=[1,2,3,4,5,6]
list2=['a','b','c','d','e','f']

list3=[]
list3.append(list1)
list3.append(list2)
print(list3)


list4=[]
for i in range(6):
    list4.append(list(list(zip(*list3))[i]))
print(list4)
