from datetime import datetime as dt
import speech_recognition as sr
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',210)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print("Clearing the background noices..Please Wait!")
        recognizer.adjust_for_ambient_noise(source, 0.5)
        print("Ask me anything.....")
        recordedauio=recognizer.listen(source)

    try:
        text=recognizer.recognize_google(recordedauio,language='en_US')
        text=text.lower()
        print('Your message:',format(text))


        if 'hello' in text:
                msg="Hello my name is Shinchan, I am your personal assistant.."
                engine.say(msg)
                engine.runAndWait()


        if 'browser' in text:
                a='Opening Browser...'
                engine.say(a)
                engine.runAndWait()
                program="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                subprocess.Popen([program])

        if 'date' in text:
                date = dt.now()
                format_date = date.strftime("%B %d, %Y")
                time = dt.now()
                format_time = time.strftime("%I:%M:%S ")
                print(format_date)
                print(format_time)
                engine.say(format_date)
                engine.say(format_time)
                engine.runAndWait()


    except Exception as ex:
        print(ex)

    
while True:
     cmd()
