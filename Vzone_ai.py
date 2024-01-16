import speech_recognition as sr
import pyttsx3 as ttx
import pywhatkit
import pyaudio
import datetime

listener = sr.Recognizer()
engine = ttx.init()
voices = engine.getProperty('voices')
engine.setProperty('voice','french')

def parle(text):
    engine.say(text)
    engine.runAndWait()

def ecoute():
    try:
        with sr.Microphone () as source:
            print('parler ')
            voix=listener.listen(source)
            listener.energy_threshold = 5000
            command = listener.recognize_google(voix,language ='fr-FR')
            return command
    except:
        pass

def assistant():
    command = ecoute()
    if command:
        print(command)
        if 'boujour' in command:
            parle('bonjour comment ça va?')
        elif 'oui ça va et toi?' in command:
            parle('oui ça va de mon côté, comment je peux vous aider')
        elif 'mettez la chanson de ' in command:
            chanteur = command.replace('mettez la chanson de ','')
            print(chanteur)
            pywhatkit.playonyt(chanteur)
        elif 'heure' in command:
            heure = datetime.datetime.now().strftime('%H:%M')
            parle('Il est '+heure)
        elif 'ton nom' in command:
            parle("je m'appelle V_zone ")

while True:
    assistant()
