import requests

url = "http://127.0.0.1:5000/launch_browser"

request_data = {
    "command": "open_url",
    "url": "https://www.example.com"
}

response = requests.post(url, json=request_data)

if response.status_code == 200:
    print("Response from Microservice:", response.json())
else:
    print("Error:", response.status_code, response.text)
