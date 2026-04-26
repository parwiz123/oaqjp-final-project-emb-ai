"""Flask server for Emotion Detection application."""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Home route for the API."""
    return "Emotion Detection API is running."


@app.route("/emotionDetector")
def detect_emotion():
    """Detect emotions from input text using Watson NLP API."""

    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid input! Text cannot be empty."

    result = emotion_detector(text_to_analyze)

    response = (
        f"For the given statement, the system response is "
        f"anger: {result['anger']}, "
        f"disgust: {result['disgust']}, "
        f"fear: {result['fear']}, "
        f"joy: {result['joy']}, "
        f"sadness: {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    