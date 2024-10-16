import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

class LogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Path to your log file
        self.log_file_path = '/path/to/your/logfile.log'

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
                    await self.send(line)
                else:
                    await asyncio.sleep(1)  # Wait before checking for new lines
        except asyncio.CancelledError:
            pass
