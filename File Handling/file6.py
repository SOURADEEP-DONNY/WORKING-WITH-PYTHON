f=open("pro.txt","r")
s=f.readlines()
l=len(s)
print(s,end="")
print("The no.of lines in txt file is: ",l)
f.close()
