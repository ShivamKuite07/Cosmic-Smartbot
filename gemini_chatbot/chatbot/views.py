from django.shortcuts import render
from django.http import JsonResponse
from .gemini_chat import chat_with_gemini

# Render the index.html
def index(request):
    return render(request, 'index.html')

# Chatbot API view for AJAX requests
def chat(request):
    user_input = request.GET.get('message', '')
    if user_input:
        response = chat_with_gemini(user_input)
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Please provide a message.'})
