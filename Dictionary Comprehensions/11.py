d={}
for i in range(10):
    d[i]=i**2
print(d)

# Same code using Dictionary Comprehension
dict1={p:p**2 for p in range(10)}
print(dict1)

#Taking User input
list11=[int(i) for i in input().split()]
di={n:n**2 for n in list11}
print(di)


#Taking User input with condition
list11=[int(i) for i in input().split()]
di={n:n**2 for n in list11 if (n**2)%2==0}
print(di)
