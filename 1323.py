#1+2+5+6
n=input("enter a number:1256")
l=len(n) #4
s=0
for i in range(1,l+1):      #i=0 n[0]=1 i=2 n[2]=2 i=3 n[3]=5 i=4 n[4]=6
    t=int(n[i])
    s=s+t
print(s)    
    
