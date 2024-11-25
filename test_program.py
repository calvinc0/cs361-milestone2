import requests

# Define the URL of your microservice
url = "http://127.0.0.1:5000/launch_browser"

# Example data to send to the microservice
request_data = {
    "command": "open_url",
    "url": "https://www.example.com"
}

# Make a POST request to the microservice
response = requests.post(url, json=request_data)

# Print the response from the microservice
if response.status_code == 200:
    print("Response from Microservice:", response.json())
else:
    print("Error:", response.status_code, response.text)
