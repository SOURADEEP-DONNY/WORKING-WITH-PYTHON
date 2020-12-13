f=open("pro.txt","r")
def stats(f):
    longest=""
    for line in file(f):
        if len(line)>len(longest):
            longest=line
    print("Longest line's Length: ",len(longest))
    print(longest)
        
