n=int(input())
b=list(input())
g=list(input())
for i in b:
    if i in g:
        g. remove(i)
    else:
        break
print(len(g), end=" " )
