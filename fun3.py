def gt(a,b):
    if(a>b):
        return a
    else:
        return b
def sm(q,z):
    if(q>z):
        return z
    else:
        return q
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
g=gt(x,y)
s=sm(x,y)
print("Greatest number: ",g)
print("Smallest number: ",s)
