a=['s','z','a','o']
b=[45,1,78,1]
data=dict(zip(a,b))
mini=min(b)
for i in data:
    if mini==data[i]:
        print(i)
