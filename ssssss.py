str1=input()
str2=input()
k=str1.strip()
k2=str2.strip()
while k2 in k:
    k=k.replace(k2,'')
l=len(k)
print(l)
