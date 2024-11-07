from temporalio import workflow
from activities import parse_message, process_message_data, acknowledge_message


@workflow.defn
class MessageProcessingWorkflow:
    @workflow.run
    async def run(self, message: str):
        # Parse the Kafka message
        parsed_data = await workflow.execute_activity(parse_message, message)

        # Process the parsed data
        await workflow.execute_activity(process_message_data, parsed_data)

        # Acknowledge the message after successful processing
        await workflow.execute_activity(acknowledge_message, message)
