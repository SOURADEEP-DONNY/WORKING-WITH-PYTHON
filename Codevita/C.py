from itertools import product
lower_limit,higher_limit=[int(i) for i in input().split()]
K=int(input())
list1=[]
def sets(n):
    addition=0
    for i in range(len(n)):
        addition=addition+int(n[i])
    return addition
for i in range(lower_limit,int(higher_limit)+1):
    list1.append(str(i))
Final__result=0
matched_sets=product(list1,repeat=K)
for z in matched_sets:
    if (sets(z)%2==0):
        Final__result=Final__result+1
print(Final__result)
