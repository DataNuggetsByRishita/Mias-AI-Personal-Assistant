import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QThread
from Terminal2 import Ui_Form
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import os
import time
import pyttsx3
import pyautogui
import pyglet
import pythoncom
import subprocess

class MiasFeatures:
    GREETINGS = ["hello Meaas", "Meaas", "wake up Meaas", "you there Meaas", "time to work Meaas", "hey Meaas",
                 "ok Meaas", "are you there"]
    GREETINGS_RES = ["always there for you ma'am", "I am ready ma'am",
                     "your wish is my command", "how can I help you ma'am?", "I am online and ready ma'am"]

    def speak(self, text):
        pythoncom.CoInitialize()  # Initialize the COM library
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(f"{text}")
        pythoncom.CoUninitialize()

    def take_commands(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.pause_threshold = 2
            audio = recognizer.listen(source, timeout=10)
            try:
                query = recognizer.recognize_google(audio, language="en-in")
                print(f"User said: {query}")
                return query
            except Exception as e:
                return "Unable to understand, say it again......"

    def open_google(self):
        self.speak("Opening Google. Just hold on a moment.")
        webbrowser.get("chrome").open("https://www.google.com")

    def open_youtube(self):
        time.sleep(2)
        webbrowser.open("https://www.youtube.com")
        self.speak("Opening YouTube. Just hold on a moment.")

    def search_google(self, query):
        self.speak(f"Searching Google for {query}.")
        webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")

    def startup(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good Morning")
        elif 12 <= hour < 18:
            self.speak("Good afternoon")
        else:
            self.speak("Good evening")
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.speak(f"Currently, it is {current_time}")
        self.speak("I am Meaas. Online and ready ma'am. Please tell me how may I help you")

    def execute_command(self, query):
        if "Open Google" in query:
            self.open_google()
        elif "Open YouTube" in query:
            self.open_youtube()

        sites = [
            ["youtube", "https://youtube.com"],
            ["Google", "https://google.com"],
            ["wikipedia", "https://wikipedia.com"],
            ["Chandigarh university management system", "https://uims.cuchd.in/"],
            ["Gmail Account", "https://mail.google.com/mail/u/0/#inbox"]
        ]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                self.speak(f"Opening {site[0]}. Just hold on a minute.")
                webbrowser.open(site[1])

            elif f"search {site[0]} for" in query.lower():
                search_query = query.lower().replace(f"search {site[0]} for", "").strip()
                self.speak(f"Searching {site[0]} for {search_query}.")
                webbrowser.open(f"https://www.google.com/search?q={search_query.replace(' ', '+')}")

        if query.lower().startswith("search on google for "):
            search_query = query.lower().replace("search on google for", "").strip()
            self.search_google(search_query)

        # Add more commands as needed
        songs = {"calm down": r"C:\Users\RISHITA\Music\Calm-Down-.mp3",
                 "right now": r"C:\Users\RISHITA\Music\Right_now.mp3"}
        if "play a song" in query.lower():
            self.speak("Which song should I play?")
            song_query = self.take_commands().lower()

            for song_name, song_path in songs.items():
                if f"play {song_name.lower()}" in song_query:
                    player = pyglet.media.Player()
                    song = pyglet.media.load(song_path)
                    player.queue(song)
                    
                    self.speak(f"Playing {song_name}.")
                    player.play()
                     # Let the song play
                    
                    
                    while True:
                        if "stop the song" in self.take_commands().lower():
                            player.pause()
                            self.speak("Stopping the song.")
                            break
                    return

        if "open camera" in query.lower():
            try:
                os.system("start microsoft.windows.camera:")
                self.speak("opening the camera application")
                time.sleep(2)
            except Exception as e:
                self.speak("sorry not able to open it")

        if "open explorer" in query.lower():
            try:
                os.system("start explorer")
                self.speak("opening file explorer")
            except Exception as e:
                self.peak("sorry not able to open it")

        elif "open command prompt" in query.lower():
            try:
                os.system("start cmd")
                self.speak("opening command prompt")
            except Exception as e:
                self.speak("sorry not able to open it")

        if "open paint" in query.lower():
            npath = "C:\Windows\system32\\mspaint.exe"
            os.startfile(npath)

        if "close paint" in query.lower():
            os.system("taskkill /f /im mspaint.exe")

        if "open notepad" in query.lower():
            npath = "C:\Windows\system32\\notepad.exe"
            os.startfile(npath)

        if "type" in query:
            query = query.replace("type", " ")
            pyautogui.typewrite(f"{query}", 0.1)

        if "close notepad" in query.lower():
            os.system("taskkill /f /im notepad.exe")

        if "what is the time" in query.lower():
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"the current time is: {strftime}")

        if "shut down the PC" in query:
            os.system("shutdown /s /t 5")

        if "go to sleep" in query:
            self.speak("alright I am going to sleep")
            sys.exit()

        if "take screenshot" in query:
            self.speak("Tell me the name of the file")
            name = self.take_commands().lower()
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            self.speak("Screenshot saved")

        if "open calculator" in query.lower():
            self.speak("Opening calculator.")
            subprocess.Popen("calc.exe", shell=True)

        if "increase volume" in query.lower():
            pyautogui.press("volumeup")

        if "decrease volume" in query.lower():
            pyautogui.press("volumedown")

        if "mute volume" in query.lower():
            pyautogui.press("volumemute")

        if "increase brightness" in query.lower():
            pyautogui.press("brightnessup")

        if "decrease brightness" in query.lower():
            pyautogui.press("brightnessdown")


class MiasMain(QThread, MiasFeatures):
    def __init__(self):
        super(MiasMain, self).__init__()

    def run(self):
        self.startup()
        while True:
            print("Listening......")
            query = self.take_commands()

            if "stop listening" in query.lower():
                break

            self.execute_command(query)


class GUIJarvis(QMainWindow, Ui_Form):
    def __init__(self):
        super(GUIJarvis, self).__init__()
        self.setupUi(self)

        self.movie1 = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/jarvisfullgui.gif")
        self.label.setMovie(self.movie1)
        self.movie1.start()

        self.movie2 = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/console 2.gif")
        self.label_2.setMovie(self.movie2)
        self.movie2.start()

        self.pushButton.clicked.connect(self.close)

        self.mias_thread = MiasMain()
        self.mias_thread.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    console = GUIJarvis()
    console.show()
    sys.exit(app.exec_())
