n=input()
l=[]
l2=[]
l3=[]
l4=[]
for i in n:
    l.append(i)
for i in l:
    if i not in l2:
        l2.append(i)
    else:
        l3.append(i)
for i in l3:
    if i not in l4:
        l4.append(i)
print(n)
print('duplicate list',l4)
