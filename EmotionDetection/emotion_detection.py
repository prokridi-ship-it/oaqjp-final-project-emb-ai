"""Detect emotion using the Watson NLP service."""
import json
import requests

def emotion_detector(text_to_analyze):
    """Detect the emotion in the supplied text."""
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=headers)

    # If the response status code is 400, set all emotions to None
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # If the response status code is 200, sett all emotions to None
    if response.status_code == 200:
        # Convert the response text into a dictionary.
        response_data = json.loads(response.text)

        # Extract the emotion scores.
        emotions = response_data["emotionPredictions"][0]["emotion"]

        # Return the emotion scores along with the dominant emotion
        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": max(
                emotions,
                key=emotions.get
            )
        }

    # Handle any unexpected status code.
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }