from openai import OpenAI
import datetime

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}],
    input="What is weather going to be like tomorrow in Marlborough, CT?"
)

print(response.output_text)