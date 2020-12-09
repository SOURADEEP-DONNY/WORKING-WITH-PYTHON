f=open("pro.txt","r")
def stats(f):
    longest=""
    for i in f:
        if len(i)>len(longest):
            longest=i
            l=len(longest)
    print("longest line's length: ",l)        
    return longest
t=stats(f)         ## calling the func
print(t)
f.close()    
            
