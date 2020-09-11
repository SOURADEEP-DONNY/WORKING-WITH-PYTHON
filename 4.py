list1=['q','a','b','c','d','e','q','a','d']
list2=[]
l=len(list1)
##print(l)
for i in range(l):
    p=list1.pop()
    if p in list1:
        list2.append(p)

print(list2)
