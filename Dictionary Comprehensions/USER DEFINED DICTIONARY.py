dict1={}

item=int(input("\nEnter total number of items:-"))
for i in range(item):
    k=input("\nEnter your key")
    v=input("\nEnter your value:-")
    dict1.update({k:v})

print(dict1)
