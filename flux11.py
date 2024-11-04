import os
import time
import requests

request = requests.post(
    'https://api.bfl.ml/v1/flux-pro-1.1',
    headers={
        'accept': 'application/json',
        'x-key': os.environ.get("BFL_API_KEY"),
        'Content-Type': 'application/json',
    },
    json={
        'prompt': 'Cthulhu, the Elder God from the HP Lovecraft stories, reading the latest issue of the JVM Weekly newsletter',
        'width': 1024,
        'height': 768
    },
).json()
print(request)
request_id = request["id"]

while True:
    time.sleep(0.5)
    result = requests.get(
        'https://api.bfl.ml/v1/get_result',
        headers={
            'accept': 'application/json',
            'x-key': os.environ.get("BFL_API_KEY"),
        },
        params={
            'id': request_id,
        },
    ).json()
    if result["status"] == "Ready":
        print(f"Result: {result['result']['sample']}")
        break
    else:
        print(f"Status: {result['status']}")