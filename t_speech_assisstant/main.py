import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
import ssl
import certifi


r = sr.Recognizer()

class client:
    name = ''

    def setName(self, name):
        self.name = name

def find_reponse(queries):
    for query in queries:
        if query in voice_data:
            return True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            t_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            t_speak('Sorry, I did not get that')
        except sr.RequestError:
            t_speak('Sorry, my speech service is down')
        return voice_data.lower()

def t_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    audio_file_num = random.randint(1, 700000000)
    audio_file = 'audio-' + str(audio_file_num) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):

    # Greeting -------------------------------------------
    if find_reponse(['hey', 'hello', 'hi', 'help']): 
        t_speak('Hello there, how can I help you?')

    # Name -------------------------------------------------
    if find_reponse(['who are you', 'what is your name', 'name', 'who']):
        if client_obj.name: 
            t_speak('My name is T, and I am your helpful speech assistant!')
        else: 
            t_speak('My name is T, your speeach assistant. What is your name?')

    # get client's name
    if find_reponse(['my name is']):
        client_name = voice_data.split("is")[-1].strip()
        t_speak('Okay, I will remember that {client_name}')
        client_obj.setName(client_name)
    
    # Time -------------------------------------------------
    if find_reponse(['what time is it', 'time', 'when', 'what time']):
        t_speak(ctime())

    # Search -------------------------------------------------
    if find_reponse(['search', 'look up', 'google', 'search up']):
        search = record_audio('What do you want to search for?')
        url = 'https://google/com/search?q=' + search
        webbrowser.get().open(url)
        t_speak('Here is what I found for ' + search)

    # Location -------------------------------------------------
    if find_reponse(['location', 'how do i get to', 'find location', 'how far']):
        location = record_audio('What is the location you are looking for?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        t_speak('Here is the location of ' + location)

    # Quit -------------------------------------------------
    if find_reponse(['quit', 'done', 'exit', 'finished']):
        t_speak('Okay, I am glad I could help, see you later!')
        exit()

time.sleep(1)

client_obj = client()
while 1:
    voice_data = record_audio()
    respond(voice_data)




