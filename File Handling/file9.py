n=int(input("Enter How many Students are there in the class: "))
f=open("Marks.txt","w")
for i in range(n):
    print("Enter details For Student",(i+1),"below:")
    r=int(input("Roll no :"))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    rec=str(r)+","+name+","+str(marks)+"\n"
    f.write(rec)
f.close()    
