import datetime
import streamlit
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
# Import "chatbot" from
# chatterbot package.

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

# speak('Hi Vasanta, how are you!')
# takeVoice()
# speak('Thats great amma!')

# speak('Hi Srinivas, how are you!')
# takeVoice()
# speak('Thats great daddy!')
import os
import streamlit as st
import openai
from PIL import Image
openai.organization = "org-EAWKAvX0fNJktesxHitezbNV"
openai.api_key = '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'
#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

#openai.api_key = os.getenv("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")
openai.Model.list()
# function that takes in string argument as parameter

def comp(PROMPT, MaxToken=50, outputs=3):
	# using OpenAI's Completion module that helps execute
	# any tasks involving text
	response = openai.Completion.create(
		# model name used here is text-davinci-003
		# there are many other models available under the
		# umbrella of GPT-3
		model="text-davinci-003",
		# passing the user input
		prompt=PROMPT,
		# generated output can have "max_tokens" number of tokens
		max_tokens=MaxToken,
		# number of outputs generated in one call
		n=outputs
	)
	# creating a list to store all the outputs
	output = list()
	for k in response['choices']:
		output.append(k['text'].strip())
	return output
# prompt="Advantages of open source contributions"











while True:



    query=takeVoice().lower()
        
    if 'ai' in query:
        speak('Sure Going To AI Mode Now!')
        speak('What do you want now?')
        prompt=takeVoice().lower()
        speak(comp(prompt,MaxToken=3000,outputs=3)[0])
        
        
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
    elif 'am i good' in query:
        speak('Yeah!, soorya you are good .')
    elif 'what language do you speak' in query:
        speak('I speak in English, soorya!')

    elif 'male or female'in query:
        speak('I have no gender soorya , I am a bot, But i have a male voice. ')
    elif 'your name' in query:
        speak('My name is Jarvis and I am a Basic AI bot.')
    elif 'created you' in query:
        speak('Mr.Soorya created me')
    elif 'good job' in query:
        speak('Thank you soorya!!')
    
    elif 'list' in query:
        l=[]
        c=0
        
        speak('Tell me the items')

        for i in range(11):
            l.append(takeVoice().lower())
            if 'enough' in l:
                break


        speak('Here is your list')
        if  'enough' in l:

            l.remove('enough')
        
                
                

            
        print(l)
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

    elif 'joke' in query:
        speak('Here is the joke..')
        My_joke = pyjokes.get_joke(language="en", category="neutral") # u can change category with 'twister' and 'all'
        speak(My_joke)
        continue
    elif 'open whatsapp' in query:
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
    elif 'open notion' in query:
        code_path="C:\\Users\\MARRI SAI SOORYA\\AppData\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Notion.lnk"
        os.startfile(code_path)
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
    elif 'locate' in query:
        speak('Tell me the location')
        path="F:\chrome driver 106\chromedriver.exe"
        driver=webdriver.Chrome(path)
        user=takeVoice().lower()
        driver.get('https://www.google.com/maps/')
        search_box=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/form/div[2]/div[3]/div/input[1]")
        search_box.send_keys(user)
        search_button=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
        search_button.click()
    elif 'weather' in query:
        speak('Tell me the location')

        search_topic='weather in '+takeVoice().lower()
        search_topic=search_topic.replace(' ','+')
        path="F:\chrome driver 106\chromedriver.exe"
        browser=webdriver.Chrome(executable_path=path)
        for i in range(1):
            elements=browser.get('https://www.google.com/search?q='+search_topic+'&start'+str(i))
    elif 'play' in query:
        speak('Which song should i play')
        search_topic=takeVoice().lower()
        search_topic=search_topic.replace(' ','+')
        path="F:\chrome driver 106\chromedriver.exe"
        browser=webdriver.Chrome(executable_path=path)
        for i in range(1):
            elements=browser.get('https://www.youtube.com/results?search_query='+search_topic+'&start'+str(i))
    elif 'news' in query:
        speak('About what')

        search_topic='todays news '+takeVoice().lower()
        search_topic=search_topic.replace(' ','+')
        path="F:\chrome driver 106\chromedriver.exe"
        browser=webdriver.Chrome(executable_path=path)
        for i in range(1):
            elements=browser.get('https://www.google.com/search?q='+search_topic+'&start'+str(i))
    elif 'open github' in query:
        speak('Opening Github')
        webbrowser.open('github.com')
    elif 'open codestudio' in query:
        speak('Opening codestudio')
        webbrowser.open('https://www.codingninjas.com/codestudio')
    elif 'open kmit telescope' in query:
        speak('Opening tesellator kmit')
        webbrowser.open('http://kmitonline.com/login/index.php')
    elif 'open codechef' in query:
        speak('Opening codechef')
        webbrowser.open('https://www.codechef.com/')
    elif 'open leetcode' in query:
        speak('Opening leetcode')
        webbrowser.open('https://leetcode.com/')
    elif 'open geeks for geeks' in query:
        speak('Opening geeks for geeks')
        webbrowser.open('https://www.geeksforgeeks.org/')
    elif 'open w3schools' in query:
        speak('opening w3schools')
        webbrowser.open('https://www.w3schools.com/')
    elif 'open linkedin' in query:
        speak('opening linkedin')
        webbrowser.open('https://www.linkedin.com/feed/')
    # elif 'open' in query:
    #     speak('what should i open')

    #     search_topic=takeVoice().lower()
    #     search_topic=search_topic.replace(' ','+')
    #     path="F:\chrome driver 106\chromedriver.exe"
    #     browser=webdriver.Chrome(executable_path=path)
    #     for i in range(1):
    #         elements=browser.get('https://www.google.com/search?q='+search_topic+'&start'+str(i))
        
    elif 'stop' in query:
        speak('Ok I am stopping, Bye Soorya')
        break
