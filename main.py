import cv2
from deepface import DeepFace
import numpy as np
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from design import Ui_MainWindow
from PyQt5 import QtWidgets


# os.environ.pop("QT_QPA_PLATFORM_PLUGIN_PATH")

# Main application window
class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        # Load Ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Video stream function
        self.updateComponents()

    # Set image to image label
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.ui.mainDisplayLabel.setPixmap(QPixmap.fromImage(image))

    @pyqtSlot(str, bool)
    def emotionUpdate(self, emotion, detected):
        if detected:
            self.ui.currentDetectedLabel.setText("Person Currently Detected")
            self.ui.emotionlabel.setText("Emotion: " + emotion)
            if emotion == "happy":
                self.ui.image_label.setPixmap(QPixmap("happy-face.svg").scaled(100, 100))
            elif emotion == "sad":
                self.ui.image_label.setPixmap(QPixmap("sad-face.svg").scaled(100, 100))
            elif emotion == "angry":
                self.ui.image_label.setPixmap(QPixmap("angry-face.svg").scaled(100, 100))
            elif emotion == "disgust":
                self.ui.image_label.setPixmap(QPixmap("disgust-face.svg").scaled(100, 100))
            elif emotion == "fear":
                self.ui.image_label.setPixmap(QPixmap("fearful-face.svg").scaled(100, 100))
            else:
                self.ui.image_label.setPixmap(QPixmap("neutral-face.svg").scaled(100,100))
        else:
            self.ui.currentDetectedLabel.setText("Nobody's Detected")
            self.ui.image_label.setPixmap(QPixmap("neutral-face.svg").scaled(100,100))
            self.ui.emotionlabel.setText("Emotion: None")

    # Run thread to update images and labels
    def updateComponents(self):
        # self.ui.mainDisplayLabel.resize(720,710)
        self.ui.image_label.setPixmap(QPixmap("neutral-face.svg").scaled(100, 100))
        self.wt = WorkerThread(self)
        self.wt.ImageUpdate.connect(self.setImage)
        self.wt.emotionUpdate.connect(self.emotionUpdate)
        self.wt.start()
        self.show()


# Thread for displaying images and labels
class WorkerThread(QThread):
    ImageUpdate = pyqtSignal(QImage)
    emotionUpdate = pyqtSignal(str, bool)
    face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  # getting a haarcascade xml file
    face_cascade = cv2.CascadeClassifier()  # processing it for our project
    if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  # adding a fallback event
        print("Error loading xml file")
    video = cv2.VideoCapture(0)
    def run(self):
        while True:
            ret, frame = self.video.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  # changing the video to grayscale to make the face analisis work properly
            face = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for x, y, w, h in face:
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),1)
                # making a try and except condition in case of any errors
                try:
                    analyze = DeepFace.analyze(frame, actions=['emotion'])
                    dominant_emotion = analyze['dominant_emotion']
                    print(dominant_emotion)
                    self.emotionUpdate.emit(dominant_emotion, True)
                except:
                    print("No face")
                    self.emotionUpdate.emit("", False)

            # Update Video
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pixmap = img.scaled(900, 900, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.ImageUpdate.emit(pixmap)

    def stop(self):
        self.quit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
