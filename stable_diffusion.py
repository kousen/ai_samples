import requests
import os

key = os.environ.get("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/ultra",
    headers={
        "authorization": f"Bearer {key}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "cats in top hats and tails playing bridge",
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open("./cats_playing_bridge.png", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))