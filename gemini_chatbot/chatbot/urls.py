from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # For the web interface
    path('chat/', views.chat, name='chat'),  # For the chatbot API
]
