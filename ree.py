f=open("Abhi.txt","r")
o=f.read()
l=[]
for i in o:
    if(i.isUpper()==True):
        l=l+i
        print(i)
        
