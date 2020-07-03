def sublist(lst):
    l=len(lst)
    i=0
    lst2=[]
    str1=""
    while i<l and lst[i]!='STOP':
        lst2.append(lst[i])
        i=i+1
    return lst2
print(sublist(['run','bun','can','STOP','TT']))
def beginning(lst):
    lst2=[]
    l=len(lst)
    i=0
    while i<l and lst[i]!='bye':
        lst2.append(lst[i])
        i=i+1
    return lst2
