import google.generativeai as genai
import os

GOOGLE_API_KEY = os.environ['GOOGLEAI_API_KEY']

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model_info = genai.get_model('models/gemini-2.0-flash-exp')
print(model_info.input_token_limit, model_info.output_token_limit)

model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
prompt = "The quick brown fox jumps over the lazy dog."

response = model.generate_content(prompt)
print(response.text)
print(response.usage_metadata)

