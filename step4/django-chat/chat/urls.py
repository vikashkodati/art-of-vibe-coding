from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sessions', views.ChatSessionViewSet, basename='chatsession')
router.register(r'messages', views.MessageViewSet, basename='message')

app_name = 'chat'

urlpatterns = [
    # Web views
    path('', views.chat_list, name='chat_list'),
    path('room/<int:session_id>/', views.chat_room, name='chat_room'),

    # API endpoints
    path('api/', include(router.urls)),
    path('api/send-message/', views.send_message, name='send_message'),
]