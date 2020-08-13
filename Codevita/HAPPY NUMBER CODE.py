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

print(happy_number)
