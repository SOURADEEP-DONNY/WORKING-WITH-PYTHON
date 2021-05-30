
import collections
def func(li, n):
	res = collections.deque([])
	li.sort()
	res.append(li[0])
	for i in range(1, n):
		f = res[0]

		if(li[i] >= 2 * f ):
                      
			res.popleft()

		res.append(li[i])

	return len(res)


n = int(input()) 
arr = list(map(int,input().strip().split()))[:n] 	
print(func(arr, n))

