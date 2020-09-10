n=int(input("\nEnter total number of elements in the list"))
list1=[]
for i in range(n):
    k=int(input("\nEnter a number to insert:-"))
    list1.append(k)

list1.sort()
print("Second Highest",list1[-2])


# Can also be taken from the front is as well

n=int(input("\nEnter total number of elements in the list"))
list1=[]
for i in range(n):
    k=int(input("\nEnter a number to insert:-"))
    list1.append(k)

list1.sort(reverse=True)

# list_name[rank-1])
print("Second Highest",list1[1])
