## Test Script

import asyncio

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "EVENT_HUB_FULLY_QUALIFIED_NAMESPACE"
EVENT_HUB_NAME = "EVENT_HUB_NAME"

credential = DefaultAzureCredential()

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a credential that has correct role assigned to access
    # event hubs namespace and the event hub name.
    producer = EventHubProducerClient(
        fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENT_HUB_NAME,
        credential=credential,
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData("First event "))
        event_data_batch.add(EventData("Second event"))
        event_data_batch.add(EventData("Third event"))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Close credential when no longer needed.
        await credential.close()

asyncio.run(run())



## CONTINOUS LOGIC

# import asyncio
# import json
# from azure.eventhub import EventData
# from azure.eventhub.aio import EventHubProducerClient
# from azure.identity.aio import DefaultAzureCredential

# EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "EVENT_HUB_FULLY_QUALIFIED_NAMESPACE"
# EVENT_HUB_NAME = "EVENT_HUB_NAME"

# credential = DefaultAzureCredential()

# async def stream_data(producer, batch_size=5):
#     buffer = []
    
#     while True:
#         # Simulate receiving JSON data from a stream (replace with your actual data source)
#         json_data = {"event": f"Streamed event", "timestamp": time.time()}
#         buffer.append(json.dumps(json_data))
        
#         if len(buffer) >= batch_size:
#             # Create a batch
#             event_data_batch = await producer.create_batch()
            
#             # Add all buffered events to the batch
#             for data in buffer:
#                 event_data_batch.add(EventData(data))
            
#             # Send the batch
#             await producer.send_batch(event_data_batch)
#             print(f"Sent a batch of {len(buffer)} events.")
            
#             # Clear the buffer after sending
#             buffer.clear()
        
#         # Simulate a short delay (replace with actual streaming data delay)
#         await asyncio.sleep(1)

# async def run():
#     producer = EventHubProducerClient(
#         fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
#         eventhub_name=EVENT_HUB_NAME,
#         credential=credential,
#     )
    
#     async with producer:
#         await stream_data(producer)
    
#     await credential.close()

# asyncio.run(run())
