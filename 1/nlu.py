"""
Created on Wed Feb 23 16:57:38 2022

@author: mcaptain79
"""
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
key = 'ZdRc53L_4nsV1LOFMVW3_Gkb4ASGYCx6nbLk6-4yUcPd'
url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/5e446778-d618-4e90-9fd5-8762e37eeccf'
def angerDetector(text):
    #authentication using your id and url
    authenticator = IAMAuthenticator(key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(version='2021-03-25',authenticator=authenticator)
    natural_language_understanding.set_service_url(url)
    #recieving response
    #keywords return important keywords in text
    response = natural_language_understanding.analyze(text=text,
            features=Features(emotion = EmotionOptions())).get_result()
    emotionDict = response['emotion']['document']['emotion']
    if emotionDict['anger'] == max(emotionDict.values()):
        return True
    return False