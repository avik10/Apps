import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

name_of_app = ['Alexa', 'alexa','siri','google']


def take_command() :
    try:
        with sr.Microphone() as source:
            print('Listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            # fo name in name_of_app:
            # if 'alexa' in command:
            return(command)
    except Exception as e:
        print(e)

def check_gender() :
    talk("what is Your Gender")
    get_gender = take_command()
    print(str(get_gender))
    if 'female' in str(get_gender):
        return 0
    return 1

def check_and_action():

    command = str(take_command())
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        pywhatkit.playonyt(song)
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(time)
    if 'who' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,3)
        print(info)
        talk(info)
    if 'joke' in command:
        talk(pyjokes.get_joke('en'))


def talk(text):
    engine.say(text)
    engine.runAndWait()



if __name__ == "__main__":
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[check_gender()].id)
    engine.say('Hi Sir... What Can I DO For You')
    engine.runAndWait()
    while True:
        check_and_action()