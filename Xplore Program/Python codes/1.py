n=int(input())
list1=[]
for i in range(n):
    str1=input()
    list1.append(str1)
def check_pallindrome(list1):
    list2=[]
    for i in list1:
        if i.lower()==i[-1::-1].lower():
            list2.append(i)
    for i in list2:
        print(i)
check_pallindrome(list1)
