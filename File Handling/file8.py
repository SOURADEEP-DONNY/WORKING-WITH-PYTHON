f=open("Stud8.txt","w")
l=[]
for i in range(5):
    name=input("Enter name of student: ")
    l.append(name+'\n')
f.writelines(l)  
f.close()    
