from openai import OpenAI
import os

client = OpenAI(
    base_url='https://external.api.recraft.ai/v1',
    api_key=os.getenv('RECRAFT_API_KEY')
)

response = client.images.generate(
    prompt='a warrior cat flies a dragon into battle'
)

print(response)
# print(response.data[0].url)
