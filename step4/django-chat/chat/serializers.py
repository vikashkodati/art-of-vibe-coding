from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ChatSession, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'chat_session', 'sender', 'content', 'timestamp', 'is_read']
        read_only_fields = ['timestamp']


class ChatSessionSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    latest_message = serializers.SerializerMethodField()

    class Meta:
        model = ChatSession
        fields = ['id', 'name', 'created_at', 'updated_at', 'participants', 'is_active', 'messages', 'latest_message']
        read_only_fields = ['created_at', 'updated_at']

    def get_latest_message(self, obj):
        latest_message = obj.messages.last()
        if latest_message:
            return MessageSerializer(latest_message).data
        return None