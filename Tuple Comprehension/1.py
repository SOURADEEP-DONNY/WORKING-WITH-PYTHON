t=(i for i in range(10))
print(t)
t=1,2,3,4,5,6
print(t)

tuple1=1,2,3,[5,6,7],48
print(tuple1)


#inserting inside a tuple list
tuple1[3].append("Insert1")
print(tuple1)


#concatenation of tuples
print(t+tuple1)

#removing an entire tuple
del tuple1

#user defined tuple
l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
tup=tuple(l)
print(tup)
