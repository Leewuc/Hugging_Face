import json
import requests

API_TOKEN = ''

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query(
    {
        "inputs": {
            "question": "What's my name?",
            "context": "My name is LEE and I live in Seoul.",
        }
    }
)

print(data)