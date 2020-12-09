f=open("Stud.txt","w")
for i in range(5):
    name=input("Enter name of student: ",)
    f.write(name)
    ##f.write("\n")  For each word in name in a seperate line
f.close()    
