import requests
import json
import asyncio
from azure.eventhub import EventData

API_URL = "https://api.fda.gov/drug/event.json"
PARAMS = {"limit": 5}

class APIMockData:
    def __init__(self):
        pass

    def fetch_healthcare_api_data(self):
        print("Fetching data from the API...")
        try:
            response = requests.get(API_URL, params=PARAMS)
            if response.status_code == 200:
                print("Data fetched successfully!")
                # Return the raw JSON object (not a string)
                return response.json()
            else:
                print(f"Failed to fetch data: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    async def stream_healthcare_data(self, producer):
        print("Started streaming healthcare data to Event Hub...")
        while True:
            data = self.fetch_healthcare_api_data()
            if data:
                # Prepare a batch for the Event Hub producer
                event_data_batch = await producer.create_batch()
                print(f"Preparing batch with {len(data.get('results', []))} events...")

                # Add each event to the batch
                for record in data.get("results", []):
                    event_body = json.dumps(record)  # Serialize each event
                    try:
                        event_data_batch.add(EventData(event_body))
                        print(f"Added event: {event_body[:50]}...")  # Show first 50 chars
                    except ValueError:
                        print("Batch size exceeded. Sending current batch...")
                        await producer.send_batch(event_data_batch)
                        event_data_batch = await producer.create_batch()
                        event_data_batch.add(EventData(event_body))

                # Send the batch
                await producer.send_batch(event_data_batch)
                print(f"Batch with {len(data.get('results', []))} events sent to Event Hub.")

            # Sleep for 10 seconds before fetching new data
            await asyncio.sleep(10)
