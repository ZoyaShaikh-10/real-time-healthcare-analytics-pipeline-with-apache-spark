import requests
import time
import json

API_URL = "https://api.fda.gov/drug/event.json"
PARAMS = {"limit": 5}

response = requests.get(API_URL, params=PARAMS)
if response.status_code == 200:
    json_object = json.dumps(response.json(), indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
    print("Done")
    
else:
    print(f"Failed to fetch data: {response.status_code}")
    