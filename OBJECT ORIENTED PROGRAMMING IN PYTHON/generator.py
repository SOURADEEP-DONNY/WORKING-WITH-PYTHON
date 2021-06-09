def firstten():
    n=1
    while n<=10:
        yield n
        n=n+1
f=firstten()
for i in f:
    print(i)
