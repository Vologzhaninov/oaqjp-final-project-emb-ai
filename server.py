""" This project uses the Emotion Predict function of the IBM Watson NLP Library
    for a text emotion detection.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotion_detection():
    """ Function to run an emotion detection using the appropriate Web API """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] == "None":
        return "Invalid text! Please try again!."
    text = "For the given statement, the system response is"
    text = text + " 'anger': " + str(response['anger'])
    text = text + ", 'disgust': " + str(response['disgust'])
    text = text + ", 'fear': " + str(response['fear'])
    text = text + ", 'joy': " + str(response['joy'])
    text = text + " and 'sadness': " + str(response['sadness'])
    text = text + ". The dominant emotion is " + response['dominant_emotion'] + "."
    return text

@app.route("/")
def render_index_page():
    """ Function to render the Web App main page """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
