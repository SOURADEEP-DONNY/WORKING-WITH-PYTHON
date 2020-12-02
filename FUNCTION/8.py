a=10
y=5
def myfunc():
    y=4
    a=2
    print("y=",y,"a=",a)
    print("a+y=",a+y)

    return a+y
print("y=",y,"a=",a)
print(myfunc())
print("y=",y,"a=",a)
