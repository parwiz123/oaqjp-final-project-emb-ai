import requests

def emotion_detector(text_to_analyze):

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    body = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=body, headers=headers)

    # -------------------------
    # CASE 1: SUCCESS (200)
    # -------------------------
    if response.status_code == 200:
        data = response.json()

        emotions = data["emotionPredictions"][0]["emotion"]

        emotions["dominant_emotion"] = max(emotions, key=emotions.get)

        return emotions

    # -------------------------
    # CASE 2: BAD REQUEST (400)
    # -------------------------
    elif response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # -------------------------
    # CASE 3: OTHER ERRORS
    # -------------------------
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }