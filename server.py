"""Flask web application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze the emotion of text supplied by the web interface."""

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Render the main web page."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
