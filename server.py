from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    text = request.form.get('text','')
    result = emotion_detector(text)
    if result['dominant_emotion'] is None:
        return "Invalid input. Enter a valid statement."
    response = (f"For the given statement, the system response is "
                f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
                f"'fear': {result['fear']}, 'joy': {result['joy']} and "
                f"'sadness': {result['sadness']}. "
                f"The dominant emotion is {result['dominant_emotion']}.")
    return response

if __name__ == '__main__':
    app.run(host= 'localhost', port= 5000)