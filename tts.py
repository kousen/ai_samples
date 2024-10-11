from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="fable",
    input="""
    By default, the endpoint will output a MP3 file
    of the spoken audio but it can also be configured
    to output any of our supported formats.
    """
)

# Stream the response to a file
with open(speech_file_path, mode="wb") as f:
    for chunk in response.iter_bytes():
        f.write(chunk)
