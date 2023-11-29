import panda as pd
import pyttsx3 
import datetime
import pyaudio 
import speech_recognition as sr 
import wikipedia 
import webbrowser
import os
import smtplib
import psutil
import pyjokes
import pyautogui
import random
import requests
from pprint import pprint

import pywhatkit as pwk

MASTER = "Master"
print("Initializing Zip...")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def add(name,address):
    speak ('Enter the app name')
    name=input('enter the app name ')
    speak('Enter the address')
    address=input('enter the address')
    
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak('The current time is')
    speak(Time)

def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('The Current date is')
    speak(date)
    speak(month)
    speak(year)

def wishme():
   speak("Welcome back sir!")
   speak("the current time is")
   time()
   speak("it's the")
   date()
   hour = datetime.datetime.now().hour
   if hour >= 0 and hour<12:
       speak("Good Morning" + MASTER)
   elif hour >=12 and hour<18:
        speak("Good Afternoon" + MASTER)
   elif hour >=18 and hour <24:
        speak("Good evening" + MASTER)
   else:
        speak("Good Night" + MASTER)
   speak("Zep at your service. Please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        again=["Say that again please...","Could you repeat that please...","Couldnt quite catch you there..."]
        
        randominteger=random.randint(0, 2)
        speak(again[randominteger])
        return  "None"
    
    return query

def whatsapp():
    speak('Enter the number')
    num=(input('Enter the number'))
    num="+91"+num
    min=datetime.datetime.now().minute + 1
    pwk.sendwhatmsg(num, "Hi, how are you?",datetime.datetime.now().hour,min)
 
    print("Message Sent!")
   

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot(image_name: str):
    
    image_name = f'{image_name}.png'
    
    image = pyautogui.screenshot()
    image.save(image_name)
    return image_name
def add(name , dir):
    app=pd.DataFrame([name,dir],columns=['Name','Directories'])
    app.to_csv('Apps.csv')


def who_am_i():
     speak('You are ' + MASTER + ', a brilliant person. I love you!')
def where_born():
    speak('I was created by a Geek in Chennai.')

def how_are_you():
    speak('I am fine, Arigato. How can I help you Sir?')
def bye():
    offline=["Going offline Sir!","Goodbye Sir!","Sayonara!!!!"]
    bye=random.randint(0, 2)
    speak(offline[bye])
    quit()
        

    
speak('Initializing Zep...')
wishme()
query = takeCommand()


if __name__ == "__main__":
    wishme()
    
    
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        
        elif 'who am i' in query:
            who_am_i()
        
        elif 'where were you born' in query:
            where_born()
        
        elif 'how are you' in query:
            how_are_you()

        elif 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia...')
            print(results)
            speak(results)
        
        
        
        elif 'chrome' in query.lower():
            speak('What should I Search?')
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe '
            search = takeCommand().lower()
            webbrowser.get(chrome_path).open_new_tab(search+'.com')
        
        elif 'youtube' in query:
            speak('What should I Search?')
            search_term = takeCommand().lower()
            speak("Opening YOUTUBE!")
            webbrowser.open('https://www.youtube.com/results?search_query='+search_term)
        
       
            

        elif 'open google' in query:
            speak('What should I Search?')
            search_term = takeCommand().lower()
            speak('Searching...')
            url = 'google.com'
            chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
            webbrowser.open('https://www.google.com/search?q='+search_term)
        
        elif 'github' in query:
            speak('Opening Github Sir!')
            search_term = takeCommand().lower()
            speak('Opening your Account Sir!'
            webbrowser.open('https://www.github.com/youraccount')
        
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            joke()
        
        elif 'bye' in query:
            bye()
        elif 'word' in query:
            speak('Opening MS Word....')
            ms_word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
            os.startfile(ms_word)
        
        elif 'downloads' in query:
            speak('Opening Downloads....')
            downloads = r'C:/Users/Tech/Downloads'
            os.startfile(downloads)
        
        elif 'whatsapp' in query:
            whatsapp()
        
       
        
        elif ' visual ' in query:
            speak('Opening Visual Code....')
            vscode = r'C:/Users/Yaash/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/code.exe'
            os.startfile(vscode)
            quit()
        
        elif 'write a note' in query:
            speak("What Should i write, Sir?")
            notes = takeCommand()
            file = open('notes.txt','w')
            speak("Sir Should I include Date and Time?")
            ans = takeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak("Done taking Notes, Sir!")
            else:
                file.write(notes)
        
        elif 'show notes' in query:
            speak('Showing Notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            speak('Name Of The File')
            name= takeCommand().lower()
            screenshot(name)
            
        
        elif 'music' in query:
            speak('Artist name')
            songOrArtist =takeCommand().lower()
            if songOrArtist== "None":
                speak("Didnt quite catch it going offline")
                quit()

            else:
                pwk.playonyt(songOrArtist) 
        elif 'who are you' in query:
            speak("I am Zoya, The Smart Assistant of Yaash, Developed to help him around with his work and makes his life easier with his machine")
        elif 'who is momo' in query:
            momo()
        
        elif 'add' in query:
            add(name,dir)
            webbrowser.open('dir')
