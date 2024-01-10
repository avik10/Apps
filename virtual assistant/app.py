
import time
import os
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
def speak(text):
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)



def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as sourse:
        speak("what should i do next sir")
        audio=r.listen(sourse)          #in audio varriable store the audio from microphone
        said = ""

    try:
        speak("I am trying to find whay you want")
        said=r.recognize_google(audio)
        print("you speak want to find{}".format(query))
    except Exception as e:
        speak("i am unable to find{}".format(e))
        speak("Please tell me again..")
    return query


if __name__ == "__main__":
    text = get_audio()
    if "hello"in text:
        speak("How are you..?")
    else:
        speak("no match found")