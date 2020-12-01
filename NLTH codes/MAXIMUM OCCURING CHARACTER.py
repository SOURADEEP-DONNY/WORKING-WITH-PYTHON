test_str = input()
print ("The original string is : " + test_str) 

all_freq = {} 
for i in test_str: 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1
res = max(all_freq, key = all_freq.get) 
 
print ("Maximum of all characters is : " + str(res)) 
