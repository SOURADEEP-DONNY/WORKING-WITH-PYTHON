f=open("pro.txt","r")
f1=open("pre.txt","w")
def remove_lowercase(f):
    s=""
    for i in f:
        if(i!='abcdefghijklmnopqrstuvwxyz'):
            s=s+i
    print(s)
##    return(s)
##shutil.copyfile(f, target)

            
            
        
