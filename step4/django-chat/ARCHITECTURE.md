# Django Chat Application Architecture

## Overview

This document describes the architectural design of the Django Chat Application, a real-time messaging system built with Django, Django REST Framework, and Django Channels for WebSocket support.

## System Components

### 1. Backend Framework
- **Django 5.2.6**: Core web framework
- **Django REST Framework 3.16.1**: API development
- **Django Channels 4.3.1**: WebSocket and async support
- **Redis**: Channel layer backend for real-time messaging

### 2. Project Structure
```
django-chat/
├── chatproject/           # Django project directory
│   ├── settings.py       # Application configuration
│   ├── urls.py          # Main URL routing
│   ├── asgi.py          # ASGI configuration for WebSocket
│   └── wsgi.py          # WSGI configuration for HTTP
├── chat/                # Chat application
│   ├── models.py        # Data models
│   ├── views.py         # HTTP views and API endpoints
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # App-specific URL routing
│   ├── consumers.py     # WebSocket consumers
│   ├── routing.py       # WebSocket URL routing
│   └── templates/       # HTML templates
├── requirements.txt     # Python dependencies
└── ARCHITECTURE.md      # This documentation
```

## Database Schema

### Models and Relationships

#### ChatSession Model
```python
class ChatSession(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(User, related_name='chat_sessions')
    is_active = models.BooleanField(default=True)
```

**Purpose**: Represents a chat room/session where multiple users can participate.

**Relationships**:
- Many-to-many relationship with Django's User model
- One-to-many relationship with Message model

#### Message Model
```python
class Message(models.Model):
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
```

**Purpose**: Stores individual messages within chat sessions.

**Relationships**:
- Foreign key to ChatSession (many messages per session)
- Foreign key to User (message sender)

### Database Features
- **Ordering**: Messages ordered by timestamp, ChatSessions by last update
- **Cascade Deletion**: Messages deleted when ChatSession is deleted
- **Read Status**: Track message read status for future features

## API Endpoints and Routing

### Web Views (Traditional Django)
- `GET /` - Chat room list (chat_list view)
- `GET /room/<int:session_id>/` - Individual chat room (chat_room view)

### REST API Endpoints
- `GET /api/sessions/` - List user's chat sessions
- `POST /api/sessions/` - Create new chat session
- `GET /api/sessions/<id>/` - Get specific chat session
- `PUT/PATCH /api/sessions/<id>/` - Update chat session
- `DELETE /api/sessions/<id>/` - Delete chat session

- `GET /api/messages/?session_id=<id>` - Get messages for a session
- `POST /api/messages/` - Create new message
- `POST /api/send-message/` - Send message endpoint

### URL Configuration
```python
# Main URLs (chatproject/urls.py)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', include('chat.urls')),
]

# Chat URLs (chat/urls.py)
urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('room/<int:session_id>/', views.chat_room, name='chat_room'),
    path('api/', include(router.urls)),
    path('api/send-message/', views.send_message, name='send_message'),
]
```

## Frontend Architecture

### Template Structure
1. **base.html**: Common layout with navigation and styling
2. **list.html**: Chat room listing with creation interface
3. **room.html**: Individual chat room with message display and input

### Template Features
- **Responsive Design**: CSS-based responsive layout
- **Real-time Updates**: JavaScript WebSocket integration
- **User Authentication**: Login/logout navigation
- **Message Display**: Differentiated styling for own vs. others' messages

### JavaScript Components
- **WebSocket Connection**: Real-time message handling
- **Message Sending**: Form submission and display
- **Auto-scroll**: Automatic scroll to latest messages
- **XSS Prevention**: HTML escaping for user content

## WebSocket Integration

### Architecture Overview
```
Client Browser ←→ Django Channels ←→ Redis Channel Layer ←→ Database
```

### WebSocket Consumer (chat/consumers.py)
```python
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect()        # Join room group
    async def disconnect()     # Leave room group
    async def receive()        # Handle incoming messages
    async def chat_message()   # Broadcast to room
```

### WebSocket Routing
```python
# chat/routing.py
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<session_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
]
```

### Real-time Features
- **Group Messaging**: Users in same chat session receive real-time updates
- **Message Persistence**: All messages saved to database
- **User Identification**: Messages tagged with sender information
- **Error Handling**: Graceful handling of connection issues

## Security Considerations

### Authentication & Authorization
- **Session-based Authentication**: Django's built-in session authentication
- **Permission Checks**: Users can only access their chat sessions
- **CSRF Protection**: Enabled for form submissions
- **WebSocket Authentication**: AuthMiddlewareStack for WebSocket connections

### Data Validation
- **Input Sanitization**: DRF serializers validate all input
- **SQL Injection Prevention**: Django ORM prevents SQL injection
- **XSS Prevention**: Template auto-escaping enabled
- **Message Length Limits**: Frontend and backend validation

### Security Headers
- **XFrame Options**: Clickjacking protection
- **Security Middleware**: Django security middleware enabled

## Development Configuration

### Settings Configuration
```python
# Key development settings
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

# Channel Layers
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {"hosts": [('127.0.0.1', 6379)]},
    },
}
```

### Dependencies
- **Runtime**: Django, DRF, Channels, Redis
- **Development**: SQLite database (production should use PostgreSQL)
- **External Services**: Redis server for channel layer

## Deployment Considerations

### Production Requirements
1. **Database**: Migrate from SQLite to PostgreSQL/MySQL
2. **Redis**: Dedicated Redis instance for channel layer
3. **Static Files**: Configure static file serving (whitenoise/CDN)
4. **Security**: Update SECRET_KEY, disable DEBUG, configure ALLOWED_HOSTS
5. **ASGI Server**: Use Daphne or uvicorn for production deployment

### Scaling Considerations
1. **Horizontal Scaling**: Multiple Django instances with shared Redis
2. **Database Optimization**: Implement connection pooling
3. **Caching**: Add Redis/Memcached for database query caching
4. **Load Balancing**: Sticky sessions required for WebSocket connections

### Monitoring & Logging
1. **WebSocket Monitoring**: Track connection counts and message rates
2. **Database Monitoring**: Query performance and connection usage
3. **Error Tracking**: Implement error monitoring (Sentry, etc.)
4. **Performance Monitoring**: Track response times and throughput

## Future Enhancements

### Planned Features
1. **User Management**: Registration, profile management
2. **Message History**: Pagination and search functionality
3. **File Sharing**: Image and file upload support
4. **Notifications**: Email and push notifications
5. **Moderation**: Message moderation and user management tools

### Technical Improvements
1. **Message Encryption**: End-to-end encryption for sensitive communications
2. **Offline Support**: Message queuing for offline users
3. **Mobile API**: Enhanced API for mobile app development
4. **Analytics**: User engagement and usage analytics
5. **Performance**: Message caching and optimized queries

This architecture provides a solid foundation for a real-time chat application with room for growth and enhancement.