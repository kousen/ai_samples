# Sample base on platform.openai.com/docs/api-reference/images/create
import base64
from openai import OpenAI
client = OpenAI(organization="org-1SttFpXfcNmfVV4Xe7jVKfNG")

img = client.images.generate(
    model="gpt-image-1",
    prompt="A warrior cat rides into battle on a dragon",
    n=1,
    size="1024x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("cat_dragon_gpt_image_1.png", "wb") as f:
    f.write(image_bytes)

print("Image saved as cat_dragon_gpt_image_1.png")