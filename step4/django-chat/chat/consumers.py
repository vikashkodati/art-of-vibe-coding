import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import ChatSession, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.session_id = self.scope['url_route']['kwargs']['session_id']
        self.room_group_name = f'chat_{self.session_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        sender_id = text_data_json.get('sender_id')

        # Save message to database
        message = await self.save_message(
            session_id=self.session_id,
            sender_id=sender_id,
            content=message_content
        )

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'id': message.id,
                    'content': message.content,
                    'sender': {
                        'id': message.sender.id,
                        'username': message.sender.username
                    },
                    'timestamp': message.timestamp.isoformat(),
                    'session_id': message.chat_session.id
                }
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, session_id, sender_id, content):
        try:
            chat_session = ChatSession.objects.get(id=session_id)
            sender = User.objects.get(id=sender_id)
            message = Message.objects.create(
                chat_session=chat_session,
                sender=sender,
                content=content
            )
            return message
        except (ChatSession.DoesNotExist, User.DoesNotExist):
            return None