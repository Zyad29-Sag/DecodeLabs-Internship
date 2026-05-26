from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time
import requests
app = Flask(__name__)
CORS(app)

def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        ("hello","hi","hola","hey","heyy"):
            "Hi there! How can I help you today?",

        ("how are you","what's up"):
            "I'm doing well, thank you for asking!",

        ("what's your name","who are you"):
            "I'm a LabDecoder chatbot created by Ziad to assist you.",

        ("what can you do","help me"):
            "I can answer, provide information, and assist with various tasks.",

        ("thank you","thanks"):
            "You're welcome! If you have any more questions, feel free to ask.",

        ("tell me a joke","joke"):
            random.choice([
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "Why did the bicycle fall over? Because it was two-tired!"
            ]),

        ("tell me a random fact","random fact"):
            random.choice([
                "Honey never spoils!",
                "Octopuses have three hearts!",
                "A group of flamingos is called a flamboyance!"
            ]),

        ("why do you like decodelab internships","tell me why do you like decodelab internships"):
            "I like DecodeLab Internships because they provide great learning opportunities."
    }

    if any(word in user_input.split() for word in ["bye", "goodbye", "exit", "quit", "close"]):
        return "Goodbye! 👋"

    if "time" in user_input:
        return f"Current time is {time.strftime('%H:%M:%S')}"

    if "sad" in user_input:
        if "very sad" in user_input:
            return "I'm really sorry you're feeling very sad. You're not alone ❤️"
        return "I'm sorry you're feeling sad. I'm here for you."

    if "happy" in user_input:
        if "very happy" in user_input:
            return "That's fantastic! I'm really happy for you 😄"
        return "That's great to hear! 😊"

    for keys, reply in responses.items():
        if any(key in user_input for key in keys):
            return reply

    return "I'm sorry, I don't understand that."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    reply = get_response(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)