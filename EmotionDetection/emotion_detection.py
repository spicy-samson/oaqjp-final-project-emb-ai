import requests, json

def emotion_detector(text_to_analyze: str) -> dict:
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(URL, json=myobj, headers=header)

     # Parse the response from the API
    formatted_response = json.loads(response.text)

    emotions: dict[str, float] = formatted_response['emotionPredictions'][0]['emotion']

    # Compare all the scores with each other
    # Make a new dictionary with the highest score appended to it. 
    if response.status_code == 200:
        highest_score = 0
        for emotion in emotions: 
            if emotions[emotion] > highest_score:
                highest_score = emotions[emotion]
                highest_emotion = emotion
            
        emotions['dominant_emotion'] = highest_emotion
    
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return emotions
