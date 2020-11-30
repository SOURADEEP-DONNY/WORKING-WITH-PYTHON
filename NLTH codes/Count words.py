import re 
test_string = input()
res = len(re.findall(r'\w+', test_string)) 
print ("The number of words in string are : " + str(res)) 
