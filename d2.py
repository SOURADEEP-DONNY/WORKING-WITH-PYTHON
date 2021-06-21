rev=0
n=int(input("Enter a number: "))
n1=n
while(n>0):
    q=n//10
    r=n%10
    rev=(rev*10)+r
    n=q
if(n1==rev):
    print("Palindrome number")
else:
    print("not a palindrome number")
