import requests
import json

url = "http://127.0.0.1:5000/retell"

# Mock payload mimicking Retell's actual webhook structure
payload = {
    "event": "call_analyzed",
    "call": {
        "call_id": "call_simulated_123",
        "from_number": "+15550001234",
        "to_number": "+15559998888",
    },
    "transcript": "Hello, this is a test transcript from the webhook.",
    "user_sentiment": "Positive"
}

try:
    print(f"Sending payload to {url}...")
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
