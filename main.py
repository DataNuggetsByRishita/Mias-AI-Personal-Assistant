import speech_recognition as sr
import win32com.client
import webbrowser
import pyglet
import datetime
import os
import openai
import random
import time
import json
import wikipedia
import webbrowser
import pywhatkit as wk
import pyautogui
import time
import operator
import requests
import sys
import pyttsx3
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from Pyqt5.QtGui import *
from Pyqt5.QtWidgets import *
from PyQt5.uic import loadUiType


engine=pyttsx3.init("sapi5")

voices=engine.getProperty('voices')

engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',170)

def Speak(audio):
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()


def Take_Commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print(" LISTENING>>>>>>>>>>")
        r.pause_threshhold=1
        audio=r.listen(source)
    try:
        print("Recognizing.......")
        
        query=r.recognize_google(audio,language="en-in")
        print(f":your command :{query}\n")
    except Exception as e:
        print("say that again please")
        return "None"
    return query.lower

def Google_Search(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    Speak("Hello Rishita, How are you")
    command = Take_Commands()

    if "search" in command:
        Speak("What would you like to search for?")
        query = Take_Commands()
        if "MIAS" in query:
            print("yes ma'am")
            Speak("yes ma'am")
        elif"who are you"in query:
            print("I am MIAS I am an AI,I can do anything that my creator has programed me to do")
            Speak("I am MIAS I am an AI,I can do anything that my creator has programed me to do")
        elif "What is" in query:
            Speak("Hold on a minute,searching for you>>>>>")
            query=query.replace("what is"," ")
            results=wikipedia.summary(query,sentences=2)
            Speak("According to wikipedia....")
            print(results)
        elif "open google"in query:
            webbrowser.open('google.com')
        elif "search on google"in query:
            Speak("what should i search")
            qry=Take_Commands.lower()
            webbrowser.open(f"{qry}")
            results=wikipedia.summary(qry,sentences=1)
            Speak(results)
        elif"open Youtube"in query:
            Speak("what you'll like to watch")
            qrry=Take_Commands.lower()
            wk.playonyt(f"{qrry}")
        elif"search on youtube"in query:
            query=query.replace("search on youtube"," ")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif"close browser"in query:
            os.system("taskill / f / im msedge.exe")
        elif"close chrome"in query:
            os.system("taskill / f / im chrome.exe")
            

        elif "open camera" in query.lower():
            try:
                os.system("start microsoft.windows.camera:")
                Speak("opening the camera application")
                time.sleep(2)
            except Exception as e:
                Speak("sorry not able to open it")
                
        elif "open explorer" in query.lower():
            try:
                os.system("start explorer")
                Speak("opening file explorer")
            except Exception as e:
                Speak("sorry not able to open it")
                
        elif "open command prompt" in query.lower():
            try:
                os.system("start cmd")
                Speak("opening command prompt")
            except Exception as e:
                Speak("sorry not able to open it")
                
        elif "open paint" in query.lower():
            npath="C:\Windows\system32\\mspaint.exe"
            os.startfile("npath")
        elif "close paint" in query:
            os.system("taskill / f / im mspaint.exe")
            
        elif "open notepad" in query.lower():
            npath="C:\Windows\system32\\mnotepad.exe"
            os.startfile("npath")
        elif"type"in query:
            query=query.replace("type"," ")
            pyautogui.typewriter(f"{query}",0.1)
            
        elif "close notepad" in query:
            os.system("taskill / f / im notepad.exe")
            
        elif "what is the time" in query.lower():
            strftime= datetime.datetime.now().strftime("%H:%M:%S")
            Speak(f"the current time is: {strftime}")
            
        elif "shut down the PC"in query:
            os.system("shutdown/s /t 5")
        elif"go to sleep"in query:
            Speak("alright i am going to sleep")
            sys.exit()
        elif"take screenshots"in query:
            Speak("tell me the name of the file")
            name=Take_Commands.lower()
            time.sleep(3)
            img=pyautogui.screenshots()
            img.save(f"{name}.png")
            Speak("screenshot saved")
        elif "open calculator" in query:
            Speak("opening calculator")
            os.system("start calculator")
        elif"volume up"in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif"volume down"in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif"mute volume"in query:
            pyautogui.press("volumemute")
        elif"increase brightness"in query:
            pyautogui.press("brightnessup")
        elif"decrease brightness"in query:
                pyautogui.press("brightnessdown")
        
            
            
songs={"calm down":r"C:\Users\RISHITA\Music\Calm-Down-.mp3",
                 "right now":r"C:\Users\RISHITA\Music\Right_now.mp3"}
for song_name,song_path in songs.items():

    if f"play {song_name.lower()}" in query.lower():
        player = pyglet.media.Player()
        song = pyglet.media.load(song_path)
        player.queue(song)
        Speak(f"playing{song_name}.")
        player.play()
        pyglet.app.run() 
            
            
