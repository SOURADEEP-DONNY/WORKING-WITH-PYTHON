def gtn(n1,n2,n3):
    if(n1>n2) and (n1>n3):
        greatest=n1
        return(greatest)
    if(n2>n1) and (n2>n3):
        greatest2=n2
        return(greatest2)
    if(n3>n1) and (n3>n2):
        greatest3=n3
        return(greatest3)
a=int(input("Enter 1st no. to be checked: "))
b=int(input("Enter 2nd no. to be checked: "))
c=int(input("Enter 3rd no. to be checked: "))
t=gtn(a,b,c)
print("Geatest among the three is: ",t)
        
