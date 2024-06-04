#task 1
git clone https://github.com/username/repo.git

#task2
pip install watson-developer-cloud
from watson_developer_cloud import NaturalLanguageUnderstandingV1

from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(

    version="2018-11-16",

    authenticator=authenticator()

)


def emotion_predictor(text):

    response = natural_language_understanding.analyze(

        text=text,

        features=Features(emotion=EmotionOptions())

    )


    emotions = response["result"]["emotion"]["document"]["emotion"]

    return emotions

#task 3
def format_emotions(emotions):

    emotion_strings = [f"{emotion}: {value * 100:.2f}%" for emotion, value in emotions.items()]

    return "\n".join(emotion_strings)
def emotion_predictor(text):

    response = natural_language_understanding.analyze(

        text=text,

        features=Features(emotion=EmotionOptions())

    )


    emotions = response["result"]["emotion"]["document"]["emotion"]

    formatted_emotions = format_emotions(emotions)

    return formatted_emotions

#task 4
emotion_detection/

|-- emotion_detector.py

|-- server.py

|-- tests/

|   |-- test_emotion_detector.py

|-- __init__.py

#task 5 
import unittest

from emotion_detector import emotion_predictor


class TestEmotionDetector(unittest.TestCase):

    def test_emotion_predictor(self):

        text = "I am very happy today!"

        emotions = emotion_predictor(text)

        self.assertGreater(emotions["joy"], 0.5)


    def test_empty_input(self):

        text = ""

        with self.assertRaises(ValueError):

            emotion_predictor(text)


if __name__ == '__main__':

    unittest.main()

#task 6
from flask import Flask, request, jsonify

from emotion_detector import emotion_predictor


app = Flask(__name__)


@app.route('/emotion', methods=['POST'])

def detect_emotion():

    text = request.get_json()['text']

    emotions = emotion_predictor(text)

    return jsonify({'emotions': emotions})


if __name__ == '__main__':

    app.run(debug=True)

#task 7
# emotion_detector.py

from watson_developer_cloud import NaturalLanguageUnderstandingV1

from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions


natural_language_understanding = NaturalLanguageUnderstandingV1(

    version="2018-11-16",

    authenticator=authenticator()

)


def emotion_predictor(text):

    try:

        response = natural_language_understanding.analyze(

            text=text,

            features=Features(emotion=EmotionOptions())

        )

        emotions = response["result"]["emotion"]["document"]["emotion"]

        return emotions

    except Exception as e:

        if e.status_code == 400:

            raise ValueError("Invalid input")

        else:

            raise


# server.py

from flask import Flask, request, jsonify

from emotion_detector import emotion_predictor


app = Flask(__name__)


@app.route('/emotion', methods=['POST'])

def detect_emotion():

    text = request.get_json()['text']

    if not text:

        return jsonify({'error': 'Blank input'}), 400

    try:

        emotions = emotion_predictor(text)

        return jsonify({'emotions': emotions})

    except ValueError as e:

        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':

    app.run(debug=True)
#task 8
pylint server.py