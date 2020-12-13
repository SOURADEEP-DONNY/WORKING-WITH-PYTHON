f=open("Abhi.txt","r")
s=f.readlines()
print(s)
longest=" "
for i in s:
    if(len(i)>len(longest)):
        longest=i
        l=len(longest)
print("Longest Line: ",longest)
print("Length of longest line: ",l)
