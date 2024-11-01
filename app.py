from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import os
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # if your getting CORS type error make sure to clear your cache or use incognito mode, this is a browser issue not a server issue

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
# ***** MAIN ISSUE! *****
# Right now the issue is that all chats will share this same session because is instantiated at top level in the server, each time the server is restarted the session is reset, but while the server runs no matter how many news or times u refresh frontend they will same chat
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

# test api
# response = model.generate_content('Hello world')
# print('api response:', response)

@app.route('/')
def home():
    return "Welcome to the Flask Chatbot API!"

# ***** test function *****
# @app.route('/api/chat', methods=['POST'])
# def chat():
#     data = request.json
#     user_message = data.get('message')
#     if not user_message:
#         return jsonify({"error": "Message is required"}), 400
    
#     # Simple response for testing
#     response = f"You said: {user_message}"
#     return jsonify({"response": response})

# ***** using openai api *****
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Send the user's message to the chat session
        response = chat_session.send_message(user_message)

        if response:
            return jsonify({"response": response.text})
        else:
            return jsonify({"error": "No content generated"}), 500
        
    except Exception as e:
        print("General Error:", e)
        return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)