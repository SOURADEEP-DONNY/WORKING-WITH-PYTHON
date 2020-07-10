#FETCHING RESPONSE CONTENT USING JSONPATH
import json
import requests
import jsonpath

url="https://reqres.in/api/users?page=2"

res=requests.get(url)

#PARSING RESULT/RESPONSE TO JSON FORMAT.

json_response=json.loads(res.text)
#print(json_response)

#FETCHING A APARTICULAR VALUE.

JSON_PATH_VALUE=jsonpath.jsonpath(json_response,'total_pages')
print(JSON_PATH_VALUE[0])
