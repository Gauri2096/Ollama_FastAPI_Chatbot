from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv
from fastapi.responses import FileResponse
load_dotenv()

OLLAMA_HOST=os.getenv("OLLAMA_HOST","http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi3")
app=FastAPI()

@app.get("/")
def read_root():
    return FileResponse(os.path.join("static", "index.html"))

@app.get("/chat")
def chat(prompt: str):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3",
        "prompt": prompt,
        "stream": False
    }
    res = requests.post(url, json=payload)
    data = res.json()
    return {
        "model": data.get("model"),
        "answer": data.get("response"),
        "prompt_tokens": data.get("prompt_eval_count"),
        "completion_tokens": data.get("eval_count"),
    }
