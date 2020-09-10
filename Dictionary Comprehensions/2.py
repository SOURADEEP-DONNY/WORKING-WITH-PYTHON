#Storing Salary of different people in a dictionary.

dict1={}
for i in range(3):
    n=input("\nEnter a name:")
    s=int(input("\nEnter salary"))
    dict1[n]=s

print(dict1)

          


# Changing a list of tuples into a dictionary

lst=[(1,'Soura'),(2,'Deep'),(3,'Donny')]
dict1={k:v for k,v in lst}

print(dict1)
