import os
from openai import OpenAI

XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

completion = client.chat.completions.create(
    model="grok-beta",
    messages=[
        {"role": "user",
         "content": "What is the incantation to summon Cthulhu, "
                    "the Elder God from the HP Lovecraft stories?"},
    ],
)

print(completion.choices[0].message.content)
