# DELETING API RESOURCE

import requests


#API URL
url="https://reqres.in/api/users/2"

#DELETING THE RESOURCE

response=requests.delete(url)


print(response.status_code)
