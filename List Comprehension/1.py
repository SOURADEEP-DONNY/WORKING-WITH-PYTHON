l1=[int(i) for i in input().split()]
print(l1)
l2=[int(i) for i in range(10)]
print(l2)

list3=[int(i) for i in range(20) if i%2==0 if i%5==0] #Interprets AND logic
print(list3)

# USING if-else STATEMENTS TOEGTHER
list4=[int(i) if i%2==0 else 'odd' for i in range(10)]
print(list4)
