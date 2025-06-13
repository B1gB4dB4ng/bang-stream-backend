from django.urls import path

# Initially empty - will be populated when we create consumers
websocket_urlpatterns = []

# Example pattern that will be added later:
# from streaming_platform.apps.chat.consumers import ChatConsumer
# websocket_urlpatterns = [
#     path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
# ]
