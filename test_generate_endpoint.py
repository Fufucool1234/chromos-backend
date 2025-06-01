
import requests
import json

# Replace with local or Render URL
URL = "http://localhost:5000/generate"

# Example test payload
payload = {
    "prompt": "vibrant mediterranean wedding in spring"
}

headers = {
    "Content-Type": "application/json"
}

try:
    print(f"Sending POST to {URL} with payload: {payload}")
    response = requests.post(URL, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.json())
except Exception as e:
    print(f"Test failed with error: {str(e)}")
