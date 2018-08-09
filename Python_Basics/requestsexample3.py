import requests
import simplejson as json


url = "https://jsonplaceholder.typicode.com/posts"

# payload is the data that is sent to the URL
payload = {"title": "foo",
           "body": "bar",
           "userId": 1}
# format the payload to json
headers = {"Content-Type": "application/json; charset=UTF-8"}

response = requests.post(url, json=payload, headers=headers)

#if we want to know the header of the response
#print(response.headers)
#response json
print(response.text)
#one line json
# print(json.loads(response.text)
