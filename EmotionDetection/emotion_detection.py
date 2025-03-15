import requests
import json

def emotion_detector(text_to_analyze):
    # Run emotion detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/' \
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    # Format output
    emotion = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = dominant_emotion

    return emotion
