import requests

url = "http://127.0.0.1:5000/chat"
data = {"character": "Hulk", "user_message": "Hello, AI!"}

response = requests.post(url, json=data)
print(response.json())
