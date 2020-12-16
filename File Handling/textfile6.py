f=open("test6.txt","w")
f.write("Roll""  ""Name""  ""Class")
a='yes'
while(a=='yes'):
    r=input("Enter Roll Number: ")
    n=input("Enter Name: ")
    c=input("Enter Class: ")
    s=(r,"    ",n,"     ",c,"   ")
    f.writelines("\n")
    f.writelines(s)
    a=input("Do you want to continue?(yes/no)")
f.close()    
