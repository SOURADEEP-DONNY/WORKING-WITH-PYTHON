def printOrder(arr, n): 

	# sorting the array 
	arr.sort() 

	# printing first half in ascending 
	# order 
	for i in range(n // 2): 
		print(arr[i], end = " ") 

	# printing second half in descending 
	# order 
	for j in range(n - 1, n // 2 -1, -1) : 
		print(arr[j], end = " ") 


	
arr = [int(i) for i in input().split()] 
n = len(arr) 
printOrder(arr, n) 


