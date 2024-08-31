"""
server.py - A Flask web application for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """Handles emotion detection requests and returns the analysis result."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant emotion is None
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    sliced_dict = dict(list(response.items())[:-1])
    response_str = str(sliced_dict)[1:-1]
    highest_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is {response_str}. " \
           f"The dominant emotion is {highest_emotion}."

@app.route("/")
def index():
    """Renders the main page of the application."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    