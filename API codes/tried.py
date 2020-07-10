import requests

url="https://www.google.com/search?q=cr7&sxsrf=ALeKk02NhM_G3b1ya2WUKAsli9PQ0DjY9w:1594368041905&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiaoZ3mm8LqAhVcyTgGHdsPDxwQ_AUoAXoECCEQAw&biw=1366&bih=657"


result=requests.get(url)
print(result)
print('\n\n')
print(result.content)
