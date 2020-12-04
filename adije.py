f=open("Abhi.txt","r")
q=f.read()
d=q.split()
l=" "
s=len(l)
print(l)
for i in d:
    if(len(i)>len(l)):
        l=i
print(l)
    
