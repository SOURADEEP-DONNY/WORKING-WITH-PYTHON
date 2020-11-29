num=1
def myfunc():
    global num
    num=10
    return num
print(num)
print(myfunc())
print(num)
