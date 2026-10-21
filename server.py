"""
Deploy the emotion detection application using Flask.
"""

# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """Detect emotion from text submitted through the request."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Handle blank or missing input.
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Handle an invalid request returned by the emotion detector.
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Display the response
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Render the application's home page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    