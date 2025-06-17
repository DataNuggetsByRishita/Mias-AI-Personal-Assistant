import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog, QLineEdit
from MIASAII import Ui_MainWindow
from PyQt5 import QtGui
from Facerecog import FaceRecognitionApp
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import os
import time
import requests

import wikipedia
import pyttsx3
import pythoncom

 

def speak( text):
    pythoncom.CoInitialize()  
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)  
    pythoncom.CoUninitialize()

class MiasMainWithStartup():
    def startup(self):
        try:
           print("starting")
           speak("Initializing Meaas")
           speak("Starting all systems applications")
           speak("Installing and checking all drivers")
           speak("Calibrating and examining all the core processors")
           speak("Checking the internet connection")
           speak("Wait a moment ma'am")
           speak("All drivers are up and running")
           speak("All systems have been activated")
           speak("Now I am online")
           speak("Press Start for Face Recognition")
        except Exception as e:
            print(f"An error occurred: {e}")

        

class mainFile(QMainWindow):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main File")
        self.mainUI = Ui_MainWindow()
        self.mainUI.setupUi(self)
        self.mainUI.movie = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/7LP8.gif")
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.mainUI.movie = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/ai.gif")
        self.mainUI.label_2.setMovie(self.mainUI.movie)
        self.mainUI.label_2.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.mainUI.movie = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/cda2b820d46413ad8d0997451bafc286.gif")
        self.mainUI.label_3.setMovie(self.mainUI.movie)
        self.mainUI.label_3.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.mainUI.pushButton_3.clicked.connect(self.close)
        self.mainUI.pushButton_2.clicked.connect(self.openFaceRecognition)

    def openFaceRecognition(self):
        name_input, ok_pressed = QInputDialog.getText(self, "Enter Your Name", "Your Name:", QLineEdit.Normal, "")
        if ok_pressed and name_input.lower() == "rishita sharma" or name_input.lower() == "rishita":
            print("facerecog")
            mias = MiasMainWithStartup()
            mias.startup()
            self.face_app = FaceRecognitionApp()
            self.face_app.show()
        else:
            QMessageBox.warning(self, "Invalid Name", "Not a valid user.", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MIAS = mainFile()
    MIAS.show()
    sys.exit(app.exec_())
