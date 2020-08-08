#ACCEPT A THREE DIGIT NUMBER AND MAKE ALL POSSIBLE COMBINATIONS.
a=int(input())
b=int(input())
c=int(input())
list1=[]
list2=[]
list1.append(a)
list1.append(b)
list1.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if i != j and j != k and k != i:
                s=(str(list1[i])+str(list1[j])+str(list1[k]))
                s=int(s)
                list2.append(s)
print(list2)
                
