str1=input()
str2=input()
list2=[]
new_str=''

for i in str2:
    list2.append(i)

for i in str1:
    if i not in list2:
        new_str=new_str+i

print(new_str)
