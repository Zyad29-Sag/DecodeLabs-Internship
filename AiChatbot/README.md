# 🤖 LabDecoder — AI Chatbot

A full-stack chatbot built with **Python (Flask)** on the backend and **React** on the frontend.  
Created as an internship project at **DecodeLab**.

---

## 📁 Project Structure

```
AiChatbot/
├── chatbot-ui/             # React frontend
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│   ├── package.json
│   └── package-lock.json
├── backend.py              # Flask API server
└── chatbot.py              # Terminal chatbot (no UI needed)
```

---

## ⚙️ Prerequisites

Make sure you have these installed before running the project:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js 16+ & npm](https://nodejs.org/)

---

## 🚀 Getting Started

### Option A — Terminal Only (No UI)

If you just want to chat without running the frontend, run directly from the project root:

```bash
cd AiChatbot
python chatbot.py
```

Type your message and press Enter. Type `bye` or `exit` to quit.

---

### Option B — Full Stack (Flask + React UI)

#### 1 — Clone the repository

```bash
git clone https://github.com/your-username/AiChatbot.git
cd AiChatbot
```

#### 2 — Run the Backend (Flask)

From the `AiChatbot` root folder:

```bash
# (Recommended) Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install flask flask-cors requests

# Start the server
python backend.py
```

The backend will run at: **http://127.0.0.1:5000**

#### 3 — Run the Frontend (React)

Open a **new terminal**, then:

```bash
# Navigate to the frontend folder
cd AiChatbot/chatbot-ui

# Install dependencies
npm install

# Start the React app
npm start
```

The frontend will open at: **http://localhost:3000**

---

## 💬 Features

| Feature | Description |
|---|---|
| 👋 Greetings | Responds to hello, hi, hey, and more |
| 😄 Mood detection | Detects happy / sad messages and responds with empathy |
| 😂 Jokes | Tells random jokes on request |
| 🌍 Random facts | Shares fun facts about the world |
| 🕐 Current time | Returns the live system time |
| 👋 Goodbye | Detects exit phrases and says goodbye |

---

## 🔗 API Endpoint

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/chat` | Send a message and get a reply |

**Request body:**
```json
{ "message": "tell me a joke" }
```

**Response:**
```json
{ "reply": "Why don't scientists trust atoms? Because they make up everything!" }
```

---

## 🛠️ Built With

- **Flask** — Python web framework
- **Flask-CORS** — Cross-origin support
- **React** — Frontend UI library

---

## 👤 Author

**Ziad** — DecodeLab Internship Project