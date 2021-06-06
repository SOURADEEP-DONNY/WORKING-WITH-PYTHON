l=[i for i in range(1,11,1)]
l2=[]
l3=[]
c=0
for i in l:
    l2.append(str(i))
s=input()
for i in s:
    if i in l2:
        c=1
        l3.append(i)
if c:
    print('Yes digit present in string')
    print('Present digits are',l3)
else:
    print('No digits present in string')
