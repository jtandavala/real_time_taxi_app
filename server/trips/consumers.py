from channels.generic.websocket import AsyncJsonWebsocketConsumer

class TaxiConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
    async def disconnect(self, code):
        await super().disconnect(code)

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'echo.message':
            await self.send_json({
                'type': message_type,
                'data': content.get('data')
            })