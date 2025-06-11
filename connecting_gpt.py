import os
import requests
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or "AIzaSyCloxpP8WSctlraKQEhAxQi0kjARxzRDbo"  # fallback if .env is missing

# Google Gemini API - Updated model name
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

headers = {
    "Content-Type": "application/json"
}

def query_gemini(prompt):
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.7,
            "topK": 1,
            "topP": 1,
            "maxOutputTokens": 2048,
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return f"Unexpected format: {data}"
    else:
        return f"Error: {response.status_code} - {response.text}"

def no_memory_chat():
    print("Chat (No Memory) - Google Gemini")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = query_gemini(user_input)
        print("Bot:", result)

def memory_chat():
    print("Chat (With Memory) - Google Gemini")
    chat_history = ""
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        chat_history += f"User: {user_input}\n"
        result = query_gemini(chat_history)
        print("Bot:", result)
        chat_history += f"Bot: {result}\n"

if __name__ == "__main__":
    print("Choose Mode:")
    print("1. No Memory Chat")
    print("2. Memory Chat")
    mode = input("Enter 1 or 2: ").strip()
    if mode == "1":
        no_memory_chat()
    elif mode == "2":
        memory_chat()
    else:
        print("Invalid choice.")