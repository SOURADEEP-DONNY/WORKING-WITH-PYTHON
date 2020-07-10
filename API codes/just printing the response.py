#API URL.
#TO MAKE A REQUEST TO THE SERVER AND GET A REQUEST FROM THE SERVER
#USE 'resquest' MODULE

import requests
url="https://reqres.in/api/users?page=2"

#TO MAKE A REQUEST SEND GET REQUEST.

result=requests.get(url)

#JUST PRINTING THE RESPONSE
print(result)
