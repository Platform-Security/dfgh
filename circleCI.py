# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://api.bitbucket.org/2.0/user"

headers = {
  "Accept": "application/json",
  "Authorization": "Bearer <access_token>"
}

response = requests.request(
   "GET",
   url,
   headers=headers
)

print(response.text)