n=input("Enter a name")
f=open('pro.txt','r')
flag=0
line=f.readlines()
for w in line:
    if(w==n):
        flag=1
        break
if(flag==1):
    print("present")
else:
    print("Absent")
