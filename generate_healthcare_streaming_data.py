import requests
import time
import json

API_URL = "https://api.fda.gov/drug/event.json"
PARAMS = {"limit": 5}


class GenerateMockData:
    def __init__(self):
        pass

    def fetch_healthcare_api_data(self):
        response = requests.get(API_URL, params=PARAMS)
        if response.status_code == 200:
            response = json.dumps(response.json(), indent =4)
            return response
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None
        

    def stream_healthcare_data(self):
        while True:
            data = self.fetch_healthcare_api_data()
            if data:
                print(data)
            time.sleep(60)  # Fetch data every 60 seconds
            

# Main function to continuously fetch data from the API
if __name__ == "__main__":
    mock_data = GenerateMockData()
    mock_data.stream_healthcare_data()