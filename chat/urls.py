from django.urls import path
from .import views

urlpatterns = [
    path('chat/', views.chat_view, name='chat'),
    path('like/<int:message_id>', views.like_message, name='like'),
]