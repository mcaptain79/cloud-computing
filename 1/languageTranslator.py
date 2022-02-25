"""
Created on Tue Feb 22 19:23:29 2022

@author: mcaptain79
"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Set some variables
key = 'NjjZDlxqxk01lKKkGtJHr40pZ0huqb6HOS33SUN3RyAp'
url = 'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/e61dd886-e748-445d-b243-99be310ea020'
def translate(model,text):
    #connecting to server with url and key
    authenticator = IAMAuthenticator(key)
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    language_translator.set_service_url(url )
    #translating language
    translation = language_translator.translate(text=text,model_id=model).get_result()
    return translation['translations'][0]['translation']