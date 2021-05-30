
def Log2(x):
	return (math.log10(x) /
			math.log10(2));

# Function to check
# if x is power of 2
def isPowerOfTwo(n):
	return (math.ceil(Log2(n)) == math.floor(Log2(n)));

# Driver Code
if(isPowerOfTwo(31)):
	print("Yes");
else:
	print("No");

if(isPowerOfTwo(64)):
	print("Yes");
else:
	print("No");
	
# This code is contributed
# by mits
