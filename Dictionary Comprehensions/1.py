dict1={}
for i in range(11):
    dict1[i]=i**2
print(dict1)
# the code using dictionary comprehension

dict2={n:n*n for n in range(11)}
print(dict2)
