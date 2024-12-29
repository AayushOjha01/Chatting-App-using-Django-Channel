import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import chatGroup, Message
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await(self.channel_layer.group_discard)(
            self.room_group_name, 
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = text_data_json["username"]
        message = text_data_json["message"]

        user = await sync_to_async(User.objects.get)(username=username)
        chat_group = await sync_to_async(chatGroup.objects.get)(name=self.room_name)
        await sync_to_async(Message.objects.create)(chat_group=chat_group, user=user, content=message)

        await(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message", 
                "username": username,
                "message": message}
        )

    async def chat_message(self,event):
        username = event["username"]
        message = event["message"]
        await self.send(text_data=json.dumps({
            "username": username,
            "message" : message
            }))
