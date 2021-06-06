n=input()
l=[]
for i in n:
    l.append(int(i))
s=0
for i in l:
    s=s+(i**3)
if s==int(n):
    print('Armstrong Number')
else:
    print('Not an Armstrong number')
    
    
