import google.generativeai as genai
import os
import markdown

GOOGLE_API_KEY = os.environ['GOOGLEAI_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

client = genai.GenerativeModel('models/gemini-2.0-flash-thinking-exp')

response = client.generate_content(
    contents='Explain Reinforcement Learning in simple terms.'
)

print(markdown.markdown(response.candidates[0].content.parts[0].text))

model_info = genai.get_model('models/gemini-2.0-flash-exp')
print(model_info.input_token_limit, model_info.output_token_limit)

model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
prompt = "What are five features of Python of interest to java developers?"

response = model.generate_content(prompt)
print(response.text)
print(response.usage_metadata)
