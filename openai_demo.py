from openai import OpenAI
import datetime

client = OpenAI()

models = client.models.list()
sorted_models = sorted(models, key=lambda m: m.id)

def format_model_details(model):
    model_id = model.id
    model_created = datetime.datetime.fromtimestamp(model.created)
    return f"{model_id} {model_created}"

for sorted_model in sorted_models:
    print(format_model_details(sorted_model))

# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system",
#          "content": "You are a poetic assistant, "
#                     "skilled in explaining complex programming concepts "
#                     "with creative flair."},
#         {"role": "user",
#          "content": "Compose a poem that explains the concept of "
#                     "recursion in programming."}
#     ]
# )
#
# print(completion.choices[0].message)
