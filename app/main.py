from temporalio.worker import Worker
from temporalio.client import Client
from workflow import MessageProcessingWorkflow
import activities
import asyncio

async def main():
    # client = await Client.connect("localhost:7233")
    #
    # # Create a worker to handle workflows and activities
    # worker = Worker(
    #     client,
    #     task_queue="kafka-task-queue",
    #     workflows=[MessageProcessingWorkflow],
    #     activities=[activities.parse_message, activities.process_message_data, activities.acknowledge_message],
    # )
    # await worker.run()

    while True:
        await asyncio.sleep(3600)  # sleep for 1 hour, then repeat

# Run this in a separate terminal to start the worker
if __name__ == "__main__":
    asyncio.run(main())
