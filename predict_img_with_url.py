import requests
import json


ENDPOINT = "YOUR_CUSTOM_VISION_ENDPOINT"
prediction_key = "YOUR_CUSTOM_VISION_KEY"

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/json"
}

image_data = {
    "Url": "YOUR_URL"
}

results = requests.post(
    url=ENDPOINT, headers=headers, data=json.dumps(image_data)).json()

for pred in results['predictions']:
    print(pred['tagName'], pred['probability'])
