from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatSession, Message
from .serializers import ChatSessionSerializer, MessageSerializer


@login_required
def chat_room(request, session_id):
    chat_session = get_object_or_404(ChatSession, id=session_id)
    return render(request, 'chat/room.html', {
        'chat_session': chat_session,
        'session_id': session_id
    })


@login_required
def chat_list(request):
    chat_sessions = ChatSession.objects.filter(participants=request.user)
    return render(request, 'chat/list.html', {
        'chat_sessions': chat_sessions
    })


class ChatSessionViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSessionSerializer

    def get_queryset(self):
        return ChatSession.objects.filter(participants=self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        session_id = self.request.query_params.get('session_id')
        if session_id:
            return Message.objects.filter(
                chat_session_id=session_id,
                chat_session__participants=self.request.user
            )
        return Message.objects.none()


@api_view(['POST'])
def send_message(request):
    session_id = request.data.get('session_id')
    content = request.data.get('content')

    if not session_id or not content:
        return Response({'error': 'session_id and content are required'},
                       status=status.HTTP_400_BAD_REQUEST)

    try:
        chat_session = ChatSession.objects.get(
            id=session_id,
            participants=request.user
        )
        message = Message.objects.create(
            chat_session=chat_session,
            sender=request.user,
            content=content
        )
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ChatSession.DoesNotExist:
        return Response({'error': 'Chat session not found'},
                       status=status.HTTP_404_NOT_FOUND)
