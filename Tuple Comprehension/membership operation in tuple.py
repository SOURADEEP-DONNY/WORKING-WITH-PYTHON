l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
tup=tuple(l)
p=int(input("Input to check membership:-"))
print(p in tup)
p=int(input("Input to check membership:-"))
print(p in tup)
