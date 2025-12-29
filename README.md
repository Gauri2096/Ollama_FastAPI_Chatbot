# Local Chatbot Server (FastAPI + Ollama)

Run a private, local chatbot using **FastAPI** and **Ollama**, with a simple web chat UI.  
All prompts and responses stay on your machine—no external API calls or token costs.

---

## Features

- Local LLM via Ollama (Mistral by default; easily switch to Llama 3, Phi‑3, etc.)
- FastAPI backend with a `/chat` endpoint that forwards prompts to Ollama and returns clean JSON
- HTML/CSS/JS chat UI served by FastAPI at `/` (no separate frontend build)
- Basic chat history in the browser (messages stay in the page)

---

## Prerequisites

- Python 3.10+ installed  
- Git installed  
- Ollama installed and working

Install Ollama from the official site and make sure this works in a terminal:
```
ollama --version
```

Then pull at least one model (e.g., Mistral):
```
ollama pull mistral
```

You should be able to test:
```
ollama run mistral
```

Type something and confirm the model replies, then exit with `Ctrl + C`.

---

## Setup

### 1. Clone the repository
```
git clone https://github.com/Gauri2096/Ollama_FastAPI_Chatbot.git
cd Ollama_FastAPI_Chatbot
```

### 2. Create and activate virtual environment

**Windows (PowerShell):**
```
python -m venv .venv
.venv\Scripts\activate
```
**macOS / Linux:**
```
python -m venv .venv
source .venv/bin/activate
```
### 3. Install dependencies
```
pip install fastapi uvicorn requests python-dotenv
```

(You can omit `python-dotenv` if you’re not using a `.env` file.)

---

## Running the app

### 1. Ensure the model exists in Ollama
```
ollama pull mistral
```

### 2. Run the FastAPI server

From the project folder with the virtualenv activated:
```
uvicorn main:app --reload
```

You should see logs like:

- `Uvicorn running on http://127.0.0.1:8000`
- `Application startup complete.`

### 3. Open the chat UI

In your browser, go to:

http://localhost:8000/

- Type a message in the input box and press **Enter** or click **Send**.
- The UI calls `GET /chat?prompt=...`, FastAPI forwards the prompt to Ollama, and the response appears as chat bubbles.

You can also test the raw API directly:

http://localhost:8000/chat?prompt=hello

This returns JSON with the model’s answer and token counts.

---
