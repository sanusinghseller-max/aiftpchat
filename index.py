from fastapi import FastAPI
from fastapi.responses import FileResponse
from TTS.api import TTS
import uuid

app = FastAPI()

tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

@app.post("/speak")
async def speak(data: dict):

    text = data["text"]

    voice = data["voice"]

    out = f"audio/{uuid.uuid4()}.wav"

    tts.tts_to_file(
        text=text,
        speaker_wav=f"voices/{voice}.wav",
        language="hi",
        file_path=out
    )

    return FileResponse(out)