import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
from datetime import datetime
import pyautogui as pg
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            talk("Say something!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        talk("Problem")
    return command

def main():
    command = listen()
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'date' in command:
        now = datetime.now()
        date = now.strftime("%a,%d %b, %Y")
        talk("Date is"+date)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')
    elif 'what time is it' in command:
        now = datetime.now()
        date = now.strftime("%H %M")
        talk("Time is"+date)

    elif 'message' in command:
        talk('Can you tell me the phone number?')
        number=listen()
        talk('what is your message')
        message = listen()
        pywhatkit.sendwhatmsg_instantly("+90"+number,message)
        pg.press('enter')
        talk('your message has been sent.')
    elif 'hi' and 'hello' in command:
        talk('Hello sir')
    elif 'how are you' in command:
        talk("I'm fine sir how about you")
    elif 'shut'and 'down' in command:
        talk("After how many minutes should the computer be turned off?")
        time = listen()
        if "minute" in time:
            time = time.replace("minute","")
        time = int(time)
        os.system("shutdown -s -f -%d " %time)
        talk('PC is going to shut down after %d minute '%time)

    elif "cancel"  in command:
        os.system("shutdown /a")
        talk('it is cancelled')
    
    elif "thank" in command:
        talk("it was my pleasure")
    
    else:
        talk("I did not understand")


