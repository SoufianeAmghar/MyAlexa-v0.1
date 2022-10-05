import speech_recognition as sr
import pyttsx3 as txttospeech
import pywhatkit
import datetime
import wikipedia
import pyjokes
import logging


listener = sr.Recognizer()
engine = txttospeech.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
#talk function

def talk(text):
    engine.say(text)
    engine.runAndWait() 
#= wikipedia.summary(person,1)


def take_command():
    try:
    
        with sr.Microphone() as source:
            print("...listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if ("soufiane") in command:
                command = command.replace('soufiane','')
                print(command)


    except BaseException as e:
        logging.exception('Error in command')
        raise e
    
    return command         

def run_soufiane():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I: %M %p')
        talk('Current time is'+time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("I am not capable of understanding that type of commands yet.")
        

while True:
    run_soufiane()
        

    



