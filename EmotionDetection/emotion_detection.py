import json
import requests

def emotion_detector(text_to_analyze):
    urlres = 'https://sn-watson-emotion.labs.skills.network'
    url = urlres + '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header, timeout=60)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        emotions_dic = response_json['emotionPredictions'][0]['emotion']
        anger_score = emotions_dic['anger']
        disgust_score = emotions_dic['disgust']
        fear_score = emotions_dic['fear']
        joy_score = emotions_dic['joy']
        sadness_score = emotions_dic['sadness']
        max_score = max(emotions_dic.values())
        key_list = list(emotions_dic.keys())
        val_list = list(emotions_dic.values())
        dominant_emotion = key_list[val_list.index(max_score)]
    elif response.status_code == 400:
        anger_score = 'None'
        disgust_score = 'None'
        fear_score = 'None'
        joy_score = 'None'
        sadness_score = 'None'
        dominant_emotion = 'None'
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
