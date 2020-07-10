#GENERATING THE URL

import requests
k=input('Enter your searching image:')
d={'q':k,'tbm':'isch'}
res=requests.get("https://www.google.com/search",params=d)

print(res.url)

print(res.content)
