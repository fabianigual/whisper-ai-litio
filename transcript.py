import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


prompt = "Prompt para dar contexto al audio."

audio_file= open("/path/to/file/audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt)