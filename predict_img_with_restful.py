import requests


ENDPOINT = "YOUR_CUSTOM_VISION_ENDPOINT"
prediction_key = "YOUR_CUSTOM_VISION_KEY"
project_id = "YOUR_PROJECT_ID_INSETTING"
iteration_name = "YOUR_MODEUL_PUBLISH_AS"

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}


for i in range(1, 4):
    with open(f"./Test_data/test_img_{i}.jpg", "rb") as image_contents:
        results = requests.post(
            url=ENDPOINT, headers=headers, data=image_contents).json()

        for pred in results['predictions']:
            print(pred['tagName'], pred['probability'])

        print("==========================")
