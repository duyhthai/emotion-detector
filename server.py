from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.get("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)

    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, "
        f"'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']} and "
        f"'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}."
    )

@app.get("/")
def render_index_page():
    return render_template("index.html")

app.run(host="0.0.0.0", port=5000)