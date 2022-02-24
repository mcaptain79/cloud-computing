"""
Created on Thu Feb 24 19:45:29 2022

@author: mcaptain79
"""
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
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
    write("voice.mp3", freq, recording)
voice_recorder()