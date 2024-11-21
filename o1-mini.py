from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {
            "role": "user",
            "content": """The RealTimeTranscriber example on the AssemblyAI website
            https://www.assemblyai.com/docs/getting-started/transcribe-streaming-audio-from-a-microphone/java
            uses the Java class to transcribe voice inputs sentence by sentence.
            The result, however, prints all the previous information
            in the buffer as well as the new info.

            Please rewrite that code to print only the new information."""
        }
    ]
)

print(response.choices[0].message.content)