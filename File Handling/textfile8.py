f=open("Std7.txt","w")
f.write("Roll""    ""Name""    ""Eng""     ""Computer""    ""Maths""   ""Total""   ""Grade")
l=[]
ans='yes'
while(ans=='yes'):
    r=input("Enter Roll number: ")
    n=input("Enter Name: ")
    e=int(input("Enter marks of english: "))
    c=int(input("Enter marks of Computer: "))
    m=int(input("Enter marks of Maths: "))
    t=e+c+m
    if(t>=250):
        g="A"
    elif(t<250 and t>=200):
        g="B"
    elif(t<200 and t>=150):
        g="C"
    else:
        g="D"
    l=[r,"      ",n,"       ",str(e),"       ",str(c),"       ",str(m),"     ",str(t),"     ",g]
    f.writelines("\n")
    f.writelines(l)
    ans=input("Do you want to continue?(yes/no)")
f.close()            
