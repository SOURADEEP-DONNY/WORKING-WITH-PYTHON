def checking_happy(num):
	list1=[]
	while True:
		number = str(num)
		add=0
		for i in number:
			add =add + (int(i)*int(i))
		if add == 1:
			return True
		elif add in list1:
			return False
		list1.append(add)
		num=add

lower=int(input())
upper=int(input())
happy_number=[]
for i in range(lower,upper+1,1):
    d=checking_happy(i)
    if d == True:
        happy_number.append(i)

print('HAPPY NUMBER LIST=',happy_number)

def check_prime(n):
    count=0
    for i in range(1,n+1,1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
    else:
        return False
happy_prime_numbers=[]
for p in happy_number:
    k=check_prime(p)
    if k==True:
        happy_prime_numbers.append(p)

print('HAPPY PRIME NUMBER LIST=',happy_prime_numbers)
