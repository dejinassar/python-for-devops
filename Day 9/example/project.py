# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://(name).atlassian.net/rest/api/3/project"

API_TOKEN = ""

auth = HTTPBasicAuth("", API_TOKEN)

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=auth)

#JSON response
print(json.dumps(response.json(), indent=2))
