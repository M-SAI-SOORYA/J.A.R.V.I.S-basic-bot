import datetime

import queue
import pyttsx3
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import glob
import pyjokes
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak('Soorya is a good boy')
def wishMe():
    time=int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        speak('Good Morning!')
    elif time>=12 and time<15:
        speak('Good After Noon!')
    elif time>=15 and time<=18:
        speak('Good Evening!')
    else:
        speak('Good Night!')
    speak('Hi Soorya I am Jarvis, how may i help you!')
def takeVoice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print('User said: ',query)
    except Exception as e:
        #print(e)
        print('Say that again..')
        return 'None'
    return query



wishMe()



while True:



    query=takeVoice().lower()
    if 'wikipedia'in query:
        speak('Searching Wikipedia...')
        query=query.replace('wikipedia','')
        results=wikipedia.summary(query,sentences=2)
        speak('According to Wikipedia')
        speak(results)
    
    elif 'how are you' in query:
        speak('I am good Soorya,  How are your?')
        takeVoice()
        speak('Thats great soorya!')

    elif 'male or female'in query:
        speak('I have no gender soorya , I am a bot, But i have a male voice. ')
    elif 'open youtube' in query:
        speak('Opening Youtube')
        webbrowser.open('youtube.com')
    elif 'open google' in query:
        speak('Opening Google')
        webbrowser.open('google.com')
    elif 'open stackoverflow' in query:
        speak('Opening Stackoverflow')
        webbrowser.open('stackoverflow.com')
    elif 'open spotify' in query:
        speak('Opening spotify')
        webbrowser.open('https://open.spotify.com/playlist/54T5DjOloBIoWwGS3wX1h6?si=4f33b22119e94700')
    elif 'the time' in query:
        strtime=datetime.datetime.now().strftime('%H:%M:%S')
        speak(f'Soorya the time is : {strtime}')
    elif 'open vs code' in query:
        code_path="C:\\Users\\MARRI SAI SOORYA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'tell a joke' in query:
        speak('Here is the joke..')
        My_joke = pyjokes.get_joke(language="en", category="neutral") # u can change category with 'twister' and 'all'
        speak(My_joke)
        continue
    elif 'open whatsapp web' in query:
        speak('Opening Whatsapp Web')
        webbrowser.open('https://web.whatsapp.com/')
    
    elif 'search in google' in query:
        speak('What should I search')
        search_topic=takeVoice().lower()
        search_topic=search_topic.replace(' ','+')
        path="F:\chrome driver 106\chromedriver.exe"
        browser=webdriver.Chrome(executable_path=path)
        for i in range(1):
            elements=browser.get('https://www.google.com/search?q='+search_topic+'&start'+str(i))
        
    elif 'search in youtube' in query:
        speak('What should I search in youtube')
        path="F:\chrome driver 106\chromedriver.exe"
        driver=webdriver.Chrome(path)
        user=takeVoice().lower()
        driver.get('https://www.youtube.com')
        search_box=driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
        search_box.send_keys(user)
        search_button=driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button")
        search_button.click()
        




    elif 'stop' in query:
        speak('Ok I am stopping, Bye Soorya')
        break
    
