import requests
import os

key = os.environ.get("STABILITY_API_KEY")

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer {key}",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "A warrior cat flies a dragon into battle",
        "output_format": "png",
    },
)

if response.status_code == 200:
    with open("./cat_dragon_flying", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))