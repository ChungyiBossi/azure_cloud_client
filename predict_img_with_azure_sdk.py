
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

ENDPOINT = "YOUR_ENDPONT"
prediction_key = "YOUR_PREDICTION_KEY"
project_id = "YOUR_PROJECT_ID"
publish_iteration_name = "YOUR_ITERATIOn_NAME"

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

for i in range(1, 4):
    with open(f"./Test_data/test_img_{i}.jpg", "rb") as image_contents:
        results = predictor.classify_image(
            project_id, publish_iteration_name, image_contents.read())

        # print(results)
        # Display the results.
        for prediction in results.predictions:
            print("\t" + prediction.tag_name +
                  ": {0:.2f}%".format(prediction.probability * 100))
