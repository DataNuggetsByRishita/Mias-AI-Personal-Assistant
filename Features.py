import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import QTimer
from FILERECOG import Ui_Form
from console import GUIJarvis
import cv2
import face_recognition
from PyQt5.QtGui import QImage, QPixmap
import os
import numpy as np
from PyQt5 import QtGui
import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import time

def speak(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(f" {text}")

class FaceRecognitionApp(QWidget):
    def __init__(self):
        super(FaceRecognitionApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.movie = QtGui.QMovie("C:/Users/RISHITA/Downloads/MIASPIC/1030_ChatGPT_feat.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateFrames)

        self.videoPath = 0  # Set default video path (you may need to adjust this)
        self.capture = cv2.VideoCapture(self.videoPath)

        self.classNames = []
        self.encodeList = []

        path = "images"
        if os.path.exists(path):
            photolist = os.listdir(path)
            for cl in photolist:
                currentImage = cv2.imread(f"{path}/{cl}")
                self.classNames.append(os.path.splitext(cl)[0])
                currentImage = cv2.cvtColor(currentImage, cv2.COLOR_BGR2BGRA)
                box = face_recognition.face_locations(currentImage)
                encodeCurFrame = face_recognition.face_encodings(currentImage, box)[0]
                self.encodeList.append(encodeCurFrame)

        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton.clicked.connect(self.openGuiJarvis)

        # Start the timer to update frames automatically
        self.timer.start(0)
        QTimer.singleShot(3000, self.startup)  # Start the startup method after 3000 milliseconds (3 seconds)

    def openGuiJarvis(self):
        # Validate the user here, replace "Rishita Sharma" with your actual validation logic
        if self.validate_user("Rishita Sharma"):
             print("Opening GUI Jarvis...")
             self.hide()  # Hide the FaceRecognitionApp window
             self.gui_jarvis = GUIJarvis()  # Create an instance of GUIJarvis
             self.gui_jarvis.show()  # Show the GUIJarvis window
        else:
             QMessageBox.warning(self, "Invalid Name", "Not a valid user.", QMessageBox.Ok)


    def validate_user(self, user_name):
        # Replace this with your actual validation logic
        return user_name == "Rishita Sharma"

    def startup(self):
        speak("Welcome Rishita Sharma")
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour <= 12:
            speak("Good Morning")
        elif hour > 12 and hour < 18:
            speak("Good afternoon")
        else:
            speak("Good evening")

        c_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Currently, it is {c_time}")
        speak("I am Meaas. Press start for my services")

    def updateFrames(self):
        ret, image = self.capture.read()
        self.displayImage(image)

    def displayImage(self, image):
        image = cv2.resize(image, (291, 281))
        try:
            self.faceRecognition(image)
        except Exception as e:
            print(e)
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        outImage = outImage.rgbSwapped()
        self.ui.label_2.setPixmap(QPixmap.fromImage(outImage))
        self.ui.label_2.setScaledContents(True)

    def faceRecognition(self, image):
        faces_of_current_frame = face_recognition.face_locations(image)
        encode_current_frame = face_recognition.face_encodings(image, faces_of_current_frame)

        for encode_face, face_location in zip(encode_current_frame, faces_of_current_frame):
            match = face_recognition.compare_faces(self.encodeList, encode_face, tolerance=0.5)
            face_distance = face_recognition.face_distance(self.encodeList, encode_face)
            name = "Unknown"
            best_match_index = np.argmin(face_distance)
            if match[best_match_index]:
                name = self.classNames[best_match_index]
                y1, x2, y2, x1 = face_location
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 250, 0), 2)
                cv2.putText(image, name, (x1-6, y2+20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    face_app = FaceRecognitionApp()
    face_app.show()
    sys.exit(app.exec_())
