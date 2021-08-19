import requests

payload = {
    "shortened": "github",
    "url": "https://www.github.com"
}

r = requests.post("http://127.0.0.1:5000/create", json=payload)
print(r.text)