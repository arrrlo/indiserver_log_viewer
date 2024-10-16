import os
import json
import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer


class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Get log file path from environment variable
        self.log_file_path = os.environ.get(
            'LOG_FILE_PATH', '/indiserver_log_viewer/logs/logfile.log'
        )

        # Open the log file in read mode
        self.logfile = open(self.log_file_path, 'r')

        # Move to the end of the file
        self.logfile.seek(0, 2)

        # Start a background task to send log lines
        self.send_task = asyncio.create_task(self.send_log_lines())

    async def disconnect(self, close_code):
        self.send_task.cancel()
        self.logfile.close()

    async def send_log_lines(self):
        try:
            while True:
                line = self.logfile.readline()
                if line:
                    await self.send(json.dumps({'message': line}))
                else:
                    await asyncio.sleep(1)  # Wait before checking for new lines
        except asyncio.CancelledError:
            pass

