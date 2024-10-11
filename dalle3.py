from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    model="dall-e-3",
    prompt="""
    Celebrate the annual Running of the Chickens,
    where the chickens of the village are released
    and villagers chase them to the town square.
    """,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)