from fastapi import FastAPI
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid
import os

app = FastAPI()

# 🔥 LOAD XTTS MODEL
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/xtts_v2"
)

# 🔥 CREATE AUDIO FOLDER
os.makedirs("audio", exist_ok=True)

@app.get("/")
def home():

    return {
        "status": "Voice API Running 😎"
    }

# 🔥 SPEAK API
@app.post("/speak")
async def speak(data: dict):

    try:

        # 🔥 GET TEXT
        text = data["text"]

        # 🔥 GET VOICE NAME
        voice = data["voice"]

        # 🔥 OUTPUT FILE
        out = f"audio/{uuid.uuid4()}.wav"

        # 🔥 GENERATE VOICE
        tts.tts_to_file(
            text=text,
            speaker_wav=f"voice/{voice}.wav",
            language="hi",
            file_path=out
        )

        # 🔥 RETURN AUDIO
        return FileResponse(
            out,
            media_type="audio/wav",
            filename="voice.wav"
        )

    except Exception as e:

        return {
            "error": str(e)
        }
