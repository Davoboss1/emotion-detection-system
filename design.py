from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.0938967, y1:0.159, x2:0.826, y2:0.5395, stop:0 rgba(239, 0, 0, 255), stop:1 rgba(117, 0, 181, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily(u"Sans Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.widget = QWidget(self.frame_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(5, 16777215))
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.widget)

        self.currentDetectedLabel = QLabel(self.frame_3)
        self.currentDetectedLabel.setObjectName(u"currentDetectedLabel")
        self.currentDetectedLabel.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.currentDetectedLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.currentDetectedLabel)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.widget_2 = QWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(5, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.widget_2)

        self.emotionlabel = QLabel(self.frame_4)
        self.emotionlabel.setObjectName(u"emotionlabel")
        self.emotionlabel.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.emotionlabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.emotionlabel)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.image_label = QLabel(self.frame)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setMaximumSize(QSize(100, 100))
        self.image_label.setStyleSheet(u"background-color: transparent;")
        self.image_label.setPixmap(QPixmap(u"eds/happy-face.svg"))
        self.image_label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.image_label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 50))
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"border: none;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainDisplayLabel = QLabel(self.frame_2)
        self.mainDisplayLabel.setObjectName(u"mainDisplayLabel")
        self.mainDisplayLabel.setIndent(0)

        self.verticalLayout.addWidget(self.mainDisplayLabel)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Emotion Detection System", None))
        self.currentDetectedLabel.setText(QCoreApplication.translate("MainWindow", u"Person Currently Detected", None))
        self.emotionlabel.setText(QCoreApplication.translate("MainWindow", u"Emotion: ", None))
        self.image_label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Design by davo", None))
        self.mainDisplayLabel.setText(QCoreApplication.translate("MainWindow", u"Video", None))
    # retranslateUi


