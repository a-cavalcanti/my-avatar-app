from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from gtts import gTTS
import uuid
import os

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/api/speak")
async def speak(request: Request):
    data = await request.json()
    text = data['text']
    
    tts = gTTS(text=text, lang='pt-br')
    audio_file = f"static/audio_{uuid.uuid4()}.mp3"
    tts.save(audio_file)
    
    return {"audioUrl": f"http://localhost:8000/{audio_file}"}
