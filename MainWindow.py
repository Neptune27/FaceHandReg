# -*- coding: utf-8 -*-
import os
import time
from multiprocessing import freeze_support

import cv2

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from FaceRecognitionTrainingThread import FaceRecognitionTrainingThread
from FacialRegThread import FacialRegThread


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout = QVBoxLayout(self.mainTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainImgLabel = QLabel(self.mainTab)
        self.mainImgLabel.setObjectName(u"mainImgLabel")
        self.mainImgLabel.setMinimumSize(QSize(640, 480))
        self.mainImgLabel.setMaximumSize(QSize(640, 480))

        self.verticalLayout.addWidget(self.mainImgLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainStartButton = QPushButton(self.mainTab)
        self.mainStartButton.setObjectName(u"mainStartButton")

        self.horizontalLayout_2.addWidget(self.mainStartButton)

        self.mainStopButton = QPushButton(self.mainTab)
        self.mainStopButton.setObjectName(u"mainStopButton")

        self.horizontalLayout_2.addWidget(self.mainStopButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.mainTab, "")
        self.trainingTab = QWidget()
        self.trainingTab.setObjectName(u"trainingTab")
        self.verticalLayout_5 = QVBoxLayout(self.trainingTab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.trainingImgLable = QLabel(self.trainingTab)
        self.trainingImgLable.setObjectName(u"trainingImgLable")
        self.trainingImgLable.setMinimumSize(QSize(640, 480))
        self.trainingImgLable.setMaximumSize(QSize(640, 480))

        self.verticalLayout_5.addWidget(self.trainingImgLable)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.trainingPersonLabel = QLabel(self.trainingTab)
        self.trainingPersonLabel.setObjectName(u"trainingPersonLabel")

        self.horizontalLayout_5.addWidget(self.trainingPersonLabel)

        self.personLineEdit = QLineEdit(self.trainingTab)
        self.personLineEdit.setObjectName(u"personLineEdit")

        self.horizontalLayout_5.addWidget(self.personLineEdit)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.trainingStartButton = QPushButton(self.trainingTab)
        self.trainingStartButton.setObjectName(u"trainingStartButton")

        self.horizontalLayout_4.addWidget(self.trainingStartButton)

        self.trainingStopButton = QPushButton(self.trainingTab)
        self.trainingStopButton.setObjectName(u"trainingStopButton")

        self.horizontalLayout_4.addWidget(self.trainingStopButton)

        self.trainingTrainingButton = QPushButton(self.trainingTab)
        self.trainingTrainingButton.setObjectName(u"trainingTrainingButton")

        self.horizontalLayout_4.addWidget(self.trainingTrainingButton)

        self.clearDataButton = QPushButton(self.trainingTab)
        self.clearDataButton.setObjectName(u"clearDataButton")

        self.horizontalLayout_4.addWidget(self.clearDataButton)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.trainingTab, "")
        self.settingTab = QWidget()
        self.settingTab.setObjectName(u"settingTab")
        self.verticalLayout_2 = QVBoxLayout(self.settingTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget.addTab(self.settingTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 815, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)
        self.facialRecThread = FacialRegThread(MainWindow)
        self.facialRecTrainingThread = FaceRecognitionTrainingThread(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainImgLabel.setText(QCoreApplication.translate("MainWindow", u"ImgLable", None))
        self.mainStartButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mainStopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab),
                                  QCoreApplication.translate("MainWindow", u"Main", None))
        self.trainingImgLable.setText(QCoreApplication.translate("MainWindow", u"ImgLable", None))
        self.trainingPersonLabel.setText(QCoreApplication.translate("MainWindow", u"Person: ", None))
        self.trainingStartButton.setText(QCoreApplication.translate("MainWindow", u"Start/Capture", None))
        self.trainingStopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.trainingTrainingButton.setText(QCoreApplication.translate("MainWindow", u"Training", None))
        self.clearDataButton.setText(QCoreApplication.translate("MainWindow", u"Clear Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trainingTab),
                                  QCoreApplication.translate("MainWindow", u"Training", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab),
                                  QCoreApplication.translate("MainWindow", u"Setting", None))

    # retranslateUi

    @Slot(QImage)
    def setImage(self, image):
        if self.tabWidget.currentWidget() == self.mainTab:
            self.mainImgLabel.setPixmap(QPixmap.fromImage(image))
        else:
            self.trainingImgLable.setPixmap(QPixmap.fromImage(image))

    def customConnect(self):
        self.facialRecThread.updateFrame.connect(self.setImage)
        self.mainStartButton.clicked.connect(self.startFR)
        self.trainingStartButton.clicked.connect(self.startRecordTraining)
        self.mainStopButton.clicked.connect(self.stopFR)
        self.trainingStopButton.clicked.connect(self.stopFR)
        self.personLineEdit.textChanged.connect(self.personNameChanged)
        self.clearDataButton.clicked.connect(self.clearData)
        self.trainingTrainingButton.clicked.connect(self.startTraining)

    def clearData(self):
        path = "FaceRecognition/output/embeddings.pickle"
        if not os.path.exists(path):
            with open(path, 'w'):
                pass
        else:
            os.remove(path)
            with open(path, 'w'):
                pass

    def personNameChanged(self, valueChanged: str):
        self.facialRecThread.personName = valueChanged

    def startFR(self):
        print("Starting")
        self.facialRecThread.status = True
        self.facialRecThread.isTraining = False
        self.facialRecThread.start()

    def startRecordTraining(self):
        print("Starting")
        self.facialRecThread.status = True
        self.facialRecThread.isTraining = True
        self.facialRecThread.start()

    def startTraining(self):
        self.facialRecTrainingThread.start()

    def stopFR(self):
        print("Finishing...")
        self.facialRecThread.cap.release()
        cv2.destroyAllWindows()
        self.status = False
        self.facialRecThread.terminate()
        # Give time for the thread to finish
        time.sleep(1)


if __name__ == "__main__":
    import sys

    freeze_support()
    app = QApplication(sys.argv)
    mainWindows = QMainWindow()
    mainWindowsUI = Ui_MainWindow()
    mainWindowsUI.setupUi(mainWindows)
    mainWindowsUI.customConnect()
    mainWindows.show()
    sys.exit(app.exec())
