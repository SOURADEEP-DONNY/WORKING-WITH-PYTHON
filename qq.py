import re
line='Welcome to python class.'
c=re.compile('.*t.o')
res=c.findall(line)
print(res)
