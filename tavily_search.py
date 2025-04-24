# To install: pip install tavily-python
import os
from tavily import TavilyClient

client = TavilyClient(os.getenv("TAVILY_API_KEY"))
response = client.search(
    query="Please give me some good quality reviews for the show Severance.",
    include_answer="basic"
)
print(response)