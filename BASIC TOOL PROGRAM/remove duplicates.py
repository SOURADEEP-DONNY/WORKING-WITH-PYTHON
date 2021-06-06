n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
