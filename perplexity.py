import os
from openai import OpenAI

API_KEY = os.getenv("PERPLEXITY_API_KEY")

messages = [
    {
        "role": "system",
        "content": (
            "You are an artificial intelligence assistant and you need to "
            "engage in a helpful, detailed, polite conversation with a user."
        ),
    },
    {
        "role": "user",
        "content": (
            "How many stars are in the universe?"
        ),
    },
]

client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)
print(response.choices[0].message.content)

# chat completion with streaming
# response_stream = client.chat.completions.create(
#     model="llama-3-sonar-large-32k-online",
#     messages=messages,
#     stream=True,
# )
# for response in response_stream:
#     print(response)
