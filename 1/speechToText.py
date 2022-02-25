"""
Created on Thu Feb 24 19:45:29 2022

@author: mcaptain79
"""
import sounddevice as sd
from scipy.io.wavfile import write
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
key = 'iNexc7JRWowt1rJKk4JrBYYo5HUeTo3z11_Qe5szbJSp'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/96098b92-b92a-4e1c-98b7-31a3366d57c8'
#function below is for recording the voice of the user and user just have 
def voice_recorder():
    # Sampling frequency
    freq = 44100
    # Recording duration
    duration = 10
    # Start recorder with the given values of 
    # duration and sample frequency
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    #Record audio for the given number of seconds
    sd.wait()
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("voice.wav", freq, recording)
def speech2text():
    authenticator = IAMAuthenticator(key)
    s2t = SpeechToTextV1(authenticator = authenticator)
    s2t.set_service_url(url)
    voice = open('voice.wav','rb')
    result = s2t.recognize(audio = voice, content_type = 'audio/wav').get_result()
    #for any silence it saves text in new array form
    fullText = ''
    for i in range(len(result['results'])):
        if result['results'][i]['alternatives'][0]['transcript'] != '%HESITATION':
            fullText += result['results'][i]['alternatives'][0]['transcript']
    return fullText