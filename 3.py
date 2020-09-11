n=input("\nEnter a word")
str1=" "
i=0
while i<len(n):
    if(n[i] not in str1):
        str1=str1+n[i]
        print(n[i],n.count(n[i]))
    i=i+1
