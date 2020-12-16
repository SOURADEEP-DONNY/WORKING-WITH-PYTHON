f=open("test5.txt","w")
f.write("Roll" " " "Name" " " "Class")
l=[]
a='yes'
while(a=='yes'):
    r=input("Enter Roll Number: ")
    n=input("Enter Name: ")
    c=input("Enter Class: ")
    l=[r,"    ",n,"     ",c,"   "]
    f.writelines("\n")
    f.writelines(l)
    a=input("Do you want to continue?(yes/no)")
f.close()    
