from itertools import permutations
import math

n1=int(input())
##l1=list(map(int,input().split()))
cc1=[]
s11=math.factorial(n1)//math.factorial(n1-(n1))
s21=math.factorial(n1)
math.factorial(n1-(n1-1))
cc.append(s11)
cc.append(s21)

if n1%2==0:
    t1=sum(cc1)+2
else:
    t1=sum(cc1)-1

print("%.6f"%(t1/cc1[-1]))
