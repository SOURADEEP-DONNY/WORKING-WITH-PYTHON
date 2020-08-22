def main(): 
	
	print( "HappyNumber_Demo" )
	
	print
	
	numbers = [  
		1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, # this is happy numbers
		3, 5, 9, 11, 20, 22, 25,                  			# this is unhappy numbers	
	]
	
	for number in numbers: 
		print ('happy')
			number, 
			isHappyNumber( number ) 
		)
	
	return
	
def isHappyNumber ( n ) :
	
	result = False
	
	prevSums = set()
	
	while not( result ) and n not in prevSums:
		
		prevSums.add( n )
		
		sum = 0
		while n > 0:
			sum += pow( n % 10, 2 )
			n = n / 10
		
		if sum == 1:
			result = True
		else:
			n = sum
	
	return result
	
main()
