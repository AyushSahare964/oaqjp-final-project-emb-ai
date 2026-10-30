"""Emotion detection using the Watson NLP Emotion Predict service."""
import os
import json
import requests

URL = os.environ.get(
    "WATSON_URL",
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict",
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ["anger", "disgust", "fear", "joy", "sadness"]


def emotion_detector(text_to_analyze):
    """Return the emotion scores and dominant emotion for the given text."""
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)

    if response.status_code == 400:
        result = {emotion: None for emotion in EMOTIONS}
        result["dominant_emotion"] = None
        return result

    scores = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(EMOTIONS, key=lambda e: result[e])
    return result
