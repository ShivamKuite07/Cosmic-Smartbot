import os
import google.generativeai as genai

def initialize_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config
    )

    return model

def chat_with_gemini(user_input):
    model = initialize_gemini()
    
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "hi how are you?\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "As an AI, I don't have feelings like humans do, but I'm here to help you.\n",
                ],
            },
        ]
    )
    
    response = chat_session.send_message(user_input)
    return response.text
