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
    model="sonar",
    messages=messages,
)
# print(response)


print(response.choices[0].message.content)

print("Citations:")
for index, url in enumerate(response.citations, start=1):
    print(f"{index}. {url}")

# When they are available, citations are a child element of
# the response, as a sibling to choices and usage
#
# From the github question:
# https://github.com/ppl-ai/api-discussion/discussions/54
#
# curl --request POST \
#      --url https://api.perplexity.ai/chat/completions \
#      --header 'accept: application/json' \
#      --header "authorization: Bearer ${KEY}" \
#      --header 'content-type: application/json' \
#      --data '{"model": "llama-3.1-sonar-large-128k-online", \
#               "messages": [{"role": "user", "content": \
#               "Do men really think about the roman empire a lot"}]}'  \
#| jq
#
# {
#   "id": "763eb1fd-e3ae-421c-834a-5ba5586c5919",
#   "model": "llama-3.1-sonar-large-128k-online",
#   "created": 1731028365,
#   "usage": {
#     "prompt_tokens": 10,
#     "completion_tokens": 363,
#     "total_tokens": 373
#   },
#   "citations": [
#     "https://www.wired.com/story/ask-men-about-roman-empire-tiktok-twitter-pop-culture/",
#     "https://www.georgetown.edu/news/do-men-really-think-about-the-roman-empire-every-day-this-roman-history-professor-sure-does/",
#     "https://www.washingtonpost.com/lifestyle/2023/09/14/roman-empire-trend-men-tiktok/",
#     "https://www.usatoday.com/story/opinion/columnist/2023/09/21/men-think-roman-empire-tiktok-trend-state-masculinity/70912148007/",
#     "https://www.reddit.com/r/HistoryMemes/comments/16iu9qk/men_be_honest_how_often_do_you_think_about_the/"
#   ],
#   "object": "chat.completion",
#   "choices": [
#     {
#       "index": 0,
#       "finish_reason": "stop",
#       "message": {
#         "role": "assistant",
#         "content": "The idea that men think about the Roman Empire a lot, as suggested by a recent viral trend on social media, is more complex and varied than a simple yes or no.\n\n## Viral Trend and Responses\nThe trend, which originated on platforms like TikTok and Twitter, involved women asking their male partners or friends how often they think about the Roman Empire. Some men responded that they think about it frequently, with answers ranging from \"every single day\" to \"a few times a month\"[3][4].\n\n## Diverse Perspectives\nHowever, not all men share this frequent contemplation. Many responses indicated that thinking about the Roman Empire is not a common occurrence for them. For example, one columnist expressed surprise and insecurity upon learning that some men supposedly think about the Roman Empire often, as he himself never does[4].\n\n## Influence of Media and Culture\nA significant point is that many people, regardless of gender, may think more about media and pop culture related to the Roman Empire rather than the historical empire itself. This includes films, TV shows, video games, and other forms of media that feature ancient Rome[1].\n\n## Historical Enthusiasts\nThere are indeed individuals, like Professor Josiah Osgood, who have a deep and daily interest in the Roman Empire due to their professional or personal passion for history. Osgood's interest is rooted in his academic work and a lifelong fascination with Roman history[2].\n\n## Conclusion\nIn summary, while some men do think about the Roman Empire frequently, this is not a universal trait among men. The trend seems to highlight a mix of genuine historical interest, the influence of pop culture, and perhaps some humor or exaggeration. It is not accurate to generalize that all men think about the Roman Empire a lot, as responses vary widely."
#       },
#       "delta": {
#         "role": "assistant",
#         "content": ""
#       }
#     }
#   ]
# }

# chat completion with streaming
# response_stream = client.chat.completions.create(
#     model="llama-3-sonar-large-32k-online",
#     messages=messages,
#     stream=True,
# )
# for response in response_stream:
#     print(response)
