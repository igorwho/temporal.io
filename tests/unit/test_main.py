import pytest
from unittest.mock import AsyncMock, patch
from app.main import main
from workflow import MessageProcessingWorkflow
import activities

@pytest.mark.asyncio
async def test_main():
    # Patch the Client and Worker
    with patch("main.Client.connect", new_callable=AsyncMock) as mock_client_connect, \
         patch("main.Worker", new_callable=AsyncMock) as mock_worker:

        # Mock client instance
        mock_client_instance = AsyncMock()
        mock_client_connect.return_value = mock_client_instance

        # Run the main function, which initializes the worker
        await main()

        # Verify Client.connect was called with the correct address
        mock_client_connect.assert_called_once_with("localhost:7233")

        # Verify the Worker was instantiated with the correct parameters
        mock_worker.assert_called_once_with(
            mock_client_instance,
            task_queue="kafka-task-queue",
            workflows=[MessageProcessingWorkflow],
            activities=[
                activities.parse_message,
                activities.process_message_data,
                activities.acknowledge_message
            ]
        )

        # Check that run() was called on the worker instance
        mock_worker_instance = mock_worker.return_value
        mock_worker_instance.run.assert_awaited_once()
