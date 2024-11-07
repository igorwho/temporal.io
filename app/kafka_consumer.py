from confluent_kafka import Consumer
from temporalio.client import Client
from workflow import MessageProcessingWorkflow

# Kafka configuration
KAFKA_CONFIG = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
KAFKA_TOPIC = "example_topic"


async def main():
    # Initialize Kafka consumer
    consumer = Consumer(KAFKA_CONFIG)
    consumer.subscribe([KAFKA_TOPIC])

    # Temporal client setup
    temporal_client = await Client.connect("localhost:7233")

    try:
        while True:
            msg = consumer.poll(1.0)  # Poll Kafka for messages
            if msg is None:
                continue
            if msg.error():
                print("Error:", msg.error())
                continue

            # Start a new Temporal workflow for each Kafka message
            message_text = msg.value().decode('utf-8')
            await temporal_client.start_workflow(
                MessageProcessingWorkflow.run,
                message=message_text,
                id=f"msg-{msg.offset()}",
                task_queue="kafka-task-queue",
            )

            # Manually commit the message offset after workflow start
            consumer.commit(msg)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()
