def removeDuplicate(str1, n): 
	index = 0

	for i in range(0, n): 
		for j in range(0, i + 1): 
			if (str1[i] == str1[j]): 
				break

		if (j == i): 
			str1[index] = str1[i] 
			index += 1
			
	return "".join(str1[:index]) 


str1=input()
n = len(str1) 
print(removeDuplicate(list(str1), n)) 

