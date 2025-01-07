import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from generate_healthcare_streaming_data import APIMockData

EVENT_HUB_CONNECTION_STR = "<Your-Event-Hub-Connection-String>"
EVENT_HUB_NAME = "<Your-Event-Hub-Name>"

async def main():
    print("Starting Event Hub Producer...")
    # Initialize Event Hub Producer
    producer = EventHubProducerClient.from_connection_string(
        conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME
    )

    # Initialize API Mock Data
    mock_data = APIMockData()

    async with producer:
        # Stream healthcare data and send to Event Hub
        await mock_data.stream_healthcare_data(producer)

asyncio.run(main())
