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

    # Convert the response text into a dictionary.
    response_dict = json.loads(response.text)

    # Extract the emotion scores.
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    # Find the emotion with the highest score.
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the emotion scores along with the dominant emotion
    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }