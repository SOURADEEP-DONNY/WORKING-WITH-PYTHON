list1=[x * x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(list1))
