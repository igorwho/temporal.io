from temporalio import activity

# Activity to parse the incoming Kafka message
@activity.defn
async def parse_message(message: str) -> dict:
    # Here you would parse your message, e.g., JSON decode
    # For simplicity, assuming the message is a JSON string
    import json
    return json.loads(message)

# Activity to process the data (e.g., applying business logic)
@activity.defn
async def process_message_data(parsed_data: dict):
    # Process the parsed message data
    print("Processing message data:", parsed_data)
    # Simulate processing
    import time; time.sleep(1)  # Simulate processing delay

# Activity to acknowledge the message (or log)
@activity.defn
async def acknowledge_message(message: str):
    print("Message processed and acknowledged:", message)
