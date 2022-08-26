import requests


# ENDPOINT = "YOUR_CUSTOM_VISION_ENDPOINT"
# prediction_key = "YOUR_CUSTOM_VISION_KEY"
# project_id = "YOUR_PROJECT_ID_INSETTING"
# iteration_name = "YOUR_MODEUL_PUBLISH_AS"
project_id = "e1cff77b-023e-4a11-a26a-4100e768d759"
prediction_key = "a5f101a1a95c4239ac3741664eb33b6d"
iteration_name = "Iteration1"
ENDPOINT = f"https://chungyifruitvision-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/{project_id}/classify/iterations/{iteration_name}/image"

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
