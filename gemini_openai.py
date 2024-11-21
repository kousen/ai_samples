from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv('GOOGLEAI_API_KEY'),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-1.5-flash",
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Explain to me how AI works"
        }
    ]
)

print(response.model)
print(response.usage)

with open('output.md', 'w') as file:
    file.write(response.choices[0].message.content)

