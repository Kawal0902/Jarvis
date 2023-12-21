import pyttsx3
import speech_recognition as sr
import datetime
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',150)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#voice to text  
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold= 1
        audio= r.listen(source, timeout=5, phrase_time_limit=5)


    try:
        print('Recognizing...')
        query= r.recognize_bing(audio, language='en-ln')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again please!")
        return "none"
    return query

#to wish
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('good morning sir')
    elif hour>12 and hour<18:
        speak('good afternoon sir')
    else:
        speak('good evening sir')
    speak('hello sir.Please tell me How can i help you?')


if __name__== "__main__":
    wish()
    while True:
        
        query= takecommand().lower()

        #logic building for taska

        if "open notepad" in query:
            npath= "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)
