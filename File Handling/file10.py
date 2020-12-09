f=open("Marks.txt","a")
for i in range(0,3,1):
    print("Enter details For Student",(i+1),"below:")
    r=int(input("Roll no :"))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    rec=str(r)+","+name+","+str(marks)+"\n"
    f.write(rec)
f.close()
