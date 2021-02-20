import re
line='Welcome to python class.'
c=re.compile('.*to')
res=c.findall(line)
print(res)
