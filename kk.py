def perfect(n):
  n=6  
  l=[]
  for i in range(1,int(n/2)+1):
    if n%i==0:
      l.append(i)
  if sum(l)==n:
    return True
  else:
    return False
