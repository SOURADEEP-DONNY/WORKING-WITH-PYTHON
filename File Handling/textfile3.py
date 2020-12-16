file=open("Std1.txt","w")
r=input("Enter Roll: ")
n=input("Enter Name: ")
l=[r]
l1=[n]
file.writelines(f'Roll is:{l}\nName:{l1}')
file.close()
