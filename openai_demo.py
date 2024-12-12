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
