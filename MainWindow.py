# -*- coding: utf-8 -*-
import os
import time
from functools import partial
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
                           QPalette, QPixmap, QRadialGradient, QTransform, QAction)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QMenuBar, QPushButton, QSizePolicy,
                               QStatusBar, QTabWidget, QVBoxLayout, QWidget, QToolButton, QListWidget, QScrollArea,
                               QComboBox, QMenu, QInputDialog, QFileDialog)

from FaceRecognitionTrainingThread import FaceRecognitionTrainingThread
from FacialRegThread import FacialRegThread
from Utils.Setting import Setting
from Utils.UserSetting import UserSetting


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(815, 650)
        self.MainWindow = MainWindow
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionAdd_New_Person = QAction(MainWindow)
        self.actionAdd_New_Person.setObjectName(u"actionAdd_New_Person")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.mainTab = QWidget()
        self.mainTab.setObjectName(u"mainTab")
        self.verticalLayout = QVBoxLayout(self.mainTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainImgLabel = QLabel(self.mainTab)
        self.mainImgLabel.setObjectName(u"mainImgLabel")
        self.mainImgLabel.setMinimumSize(QSize(640, 480))
        self.mainImgLabel.setMaximumSize(QSize(640, 480))
        self.mainImgLabel.setFont(font)

        self.verticalLayout.addWidget(self.mainImgLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mainStartButton = QPushButton(self.mainTab)
        self.mainStartButton.setObjectName(u"mainStartButton")
        self.mainStartButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.mainStartButton)

        self.mainStopButton = QPushButton(self.mainTab)
        self.mainStopButton.setObjectName(u"mainStopButton")
        self.mainStopButton.setFont(font)

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
        self.horizontalLayout_6 = QHBoxLayout(self.settingTab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.personWidget = QListWidget(self.settingTab)
        self.personWidget.setObjectName(u"personWidget")
        self.personWidget.setFont(font)

        self.horizontalLayout_6.addWidget(self.personWidget)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.settingTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.label = QLabel(self.settingTab)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)

        self.label_3 = QLabel(self.settingTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.scrollArea = QScrollArea(self.settingTab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 610, 503))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_4)

        self.closeCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.closeCB.addItem("")
        self.closeCB.addItem("")
        self.closeCB.addItem("")
        self.closeCB.addItem("")
        self.closeCB.addItem("")
        self.closeCB.setObjectName(u"closeCB")
        self.closeCB.setFont(font)

        self.horizontalLayout_8.addWidget(self.closeCB)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.closeLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.closeLE.setObjectName(u"closeLE")
        self.closeLE.setFont(font)

        self.horizontalLayout_3.addWidget(self.closeLE)

        self.closeOB = QToolButton(self.scrollAreaWidgetContents_2)
        self.closeOB.setObjectName(u"closeOB")
        self.closeOB.setFont(font)

        self.horizontalLayout_3.addWidget(self.closeOB)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_17.addWidget(self.label_13)

        self.openCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.openCB.addItem("")
        self.openCB.addItem("")
        self.openCB.addItem("")
        self.openCB.addItem("")
        self.openCB.addItem("")
        self.openCB.setObjectName(u"openCB")
        self.openCB.setFont(font)

        self.horizontalLayout_17.addWidget(self.openCB)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.openLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.openLE.setObjectName(u"openLE")
        self.openLE.setFont(font)

        self.horizontalLayout_9.addWidget(self.openLE)

        self.openOB = QToolButton(self.scrollAreaWidgetContents_2)
        self.openOB.setObjectName(u"openOB")
        self.openOB.setFont(font)

        self.horizontalLayout_9.addWidget(self.openOB)

        self.horizontalLayout_17.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 2)
        self.horizontalLayout_17.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_12)

        self.oneCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.oneCB.addItem("")
        self.oneCB.addItem("")
        self.oneCB.addItem("")
        self.oneCB.addItem("")
        self.oneCB.addItem("")
        self.oneCB.setObjectName(u"oneCB")
        self.oneCB.setFont(font)

        self.horizontalLayout_16.addWidget(self.oneCB)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.oneLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.oneLE.setObjectName(u"oneLE")
        self.oneLE.setFont(font)

        self.horizontalLayout_11.addWidget(self.oneLE)

        self.oneOB = QToolButton(self.scrollAreaWidgetContents_2)
        self.oneOB.setObjectName(u"oneOB")
        self.oneOB.setFont(font)

        self.horizontalLayout_11.addWidget(self.oneOB)

        self.horizontalLayout_16.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 2)
        self.horizontalLayout_16.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_11)

        self.twoCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.twoCB.addItem("")
        self.twoCB.addItem("")
        self.twoCB.addItem("")
        self.twoCB.addItem("")
        self.twoCB.addItem("")
        self.twoCB.setObjectName(u"twoCB")
        self.twoCB.setFont(font)

        self.horizontalLayout_15.addWidget(self.twoCB)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.twoLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.twoLE.setObjectName(u"twoLE")
        self.twoLE.setFont(font)

        self.horizontalLayout_12.addWidget(self.twoLE)

        self.twoOB = QToolButton(self.scrollAreaWidgetContents_2)
        self.twoOB.setObjectName(u"twoOB")
        self.twoOB.setFont(font)

        self.horizontalLayout_12.addWidget(self.twoOB)

        self.horizontalLayout_15.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 2)
        self.horizontalLayout_15.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_10)

        self.threeCB = QComboBox(self.scrollAreaWidgetContents_2)
        self.threeCB.addItem("")
        self.threeCB.addItem("")
        self.threeCB.addItem("")
        self.threeCB.addItem("")
        self.threeCB.addItem("")
        self.threeCB.setObjectName(u"threeCB")
        self.threeCB.setFont(font)

        self.horizontalLayout_14.addWidget(self.threeCB)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.threeLE = QLineEdit(self.scrollAreaWidgetContents_2)
        self.threeLE.setObjectName(u"threeLE")
        self.threeLE.setFont(font)

        self.horizontalLayout_10.addWidget(self.threeLE)

        self.threeOB = QToolButton(self.scrollAreaWidgetContents_2)
        self.threeOB.setObjectName(u"threeOB")
        self.threeOB.setFont(font)

        self.horizontalLayout_10.addWidget(self.threeOB)

        self.horizontalLayout_14.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)
        self.horizontalLayout_14.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 4)
        self.tabWidget.addTab(self.settingTab, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 815, 22))
        self.menuSetting = QMenu(self.menubar)
        self.menuSetting.setObjectName(u"menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSetting.menuAction())
        self.menuSetting.addAction(self.actionSave)
        self.menuSetting.addAction(self.actionAdd_New_Person)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionAdd_New_Person.setText(QCoreApplication.translate("MainWindow", u"Add New Person", None))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hand Type", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Extra Attribute", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.closeCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.closeCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.closeCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.closeCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.closeCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Open", None))

        self.closeOB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.openCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.openCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.openCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.openCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.openCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Open", None))

        self.openOB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"One", None))
        self.oneCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.oneCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.oneCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.oneCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.oneCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Open", None))

        self.oneOB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Two", None))
        self.twoCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.twoCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.twoCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.twoCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.twoCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Open", None))

        self.twoOB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Three", None))
        self.threeCB.setItemText(0, QCoreApplication.translate("MainWindow", u"Move Left", None))
        self.threeCB.setItemText(1, QCoreApplication.translate("MainWindow", u"Move Right", None))
        self.threeCB.setItemText(2, QCoreApplication.translate("MainWindow", u"Move Up", None))
        self.threeCB.setItemText(3, QCoreApplication.translate("MainWindow", u"Move Down", None))
        self.threeCB.setItemText(4, QCoreApplication.translate("MainWindow", u"Open", None))

        self.threeOB.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingTab),
                                  QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuSetting.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))

    # retranslateUi

    @Slot(QImage)
    def setImage(self, image):
        if self.tabWidget.currentWidget() == self.mainTab:
            self.mainImgLabel.setPixmap(QPixmap.fromImage(image))
        else:
            self.trainingImgLable.setPixmap(QPixmap.fromImage(image))

    def customConnect(self):

        self.setting = Setting()
        self.setting.load()

        self.personWidget.currentItemChanged.connect(self.onPersonWidgetClick)

        self.actionSave.triggered.connect(self.onActionSave)
        self.actionAdd_New_Person.triggered.connect(self.onActionAdd)

        self.setupSetting()

        self.facialRecThread = FacialRegThread(self.MainWindow, setting=self.setting)
        self.facialRecTrainingThread = FaceRecognitionTrainingThread(self.MainWindow)

        self.facialRecThread.updateFrame.connect(self.setImage)
        self.mainStartButton.clicked.connect(self.startFR)
        self.trainingStartButton.clicked.connect(self.startRecordTraining)
        self.mainStopButton.clicked.connect(self.stopFR)
        self.trainingStopButton.clicked.connect(self.stopFR)
        self.personLineEdit.textChanged.connect(self.personNameChanged)
        self.clearDataButton.clicked.connect(self.clearData)
        self.trainingTrainingButton.clicked.connect(self.startTraining)

        self.openCB.currentIndexChanged.connect(lambda _: self.onSettingValueChanged(self.openCB, self.openLE, "Open"))
        self.openLE.textChanged.connect(lambda _: self.onSettingValueChanged(self.openCB, self.openLE, "Open"))
        self.openOB.clicked.connect(lambda _: self.openFilePicker(self.openLE))

        self.closeCB.currentIndexChanged.connect(
            lambda _: self.onSettingValueChanged(self.closeCB, self.closeLE, "Close"))
        self.closeLE.textChanged.connect(lambda _: self.onSettingValueChanged(self.closeCB, self.closeLE, "Close"))
        self.closeOB.clicked.connect(lambda _: self.openFilePicker(self.closeLE))

        self.oneCB.currentIndexChanged.connect(lambda _: self.onSettingValueChanged(self.oneCB, self.oneLE, "One"))
        self.oneLE.textChanged.connect(lambda _: self.onSettingValueChanged(self.oneCB, self.oneLE, "One"))
        self.oneOB.clicked.connect(lambda _: self.openFilePicker(self.oneLE))

        self.twoCB.currentIndexChanged.connect(lambda _: self.onSettingValueChanged(self.twoCB, self.twoLE, "Two"))
        self.twoLE.textChanged.connect(lambda _: self.onSettingValueChanged(self.twoCB, self.twoLE, "Two"))
        self.twoOB.clicked.connect(lambda _: self.openFilePicker(self.twoLE))

        self.threeCB.currentIndexChanged.connect(
            lambda _: self.onSettingValueChanged(self.threeCB, self.threeLE, "Three"))
        self.threeLE.textChanged.connect(lambda _: self.onSettingValueChanged(self.threeCB, self.threeLE, "Three"))
        self.threeOB.clicked.connect(lambda _: self.openFilePicker(self.threeLE))

    def clearData(self):
        path = "FaceRecognition/output/embeddings.pickle"
        if not os.path.exists(path):
            with open(path, 'w'):
                pass
        else:
            os.remove(path)
            with open(path, 'w'):
                pass

    def onActionSave(self):
        self.setting.save()

    def onActionAdd(self):
        text, ok = QInputDialog.getText(None, 'Text Input Dialog', 'Enter your name:')
        if ok:
            self.setting.add(text)
            self.setupSetting()

    def onPersonWidgetClick(self, action, ignored):
        person = self.personWidget.currentItem().text()
        self.setupUserSetting(person)

    def setupUserSetting(self, person_name: str):
        try:
            person = self.setting.user[person_name]
            self.setSettingActionValue(self.openCB, self.openLE, person.Open)
            self.setSettingActionValue(self.closeCB, self.closeOB, person.Close)
            self.setSettingActionValue(self.oneCB, self.oneLE, person.One)
            self.setSettingActionValue(self.twoCB, self.twoLE, person.Two)
            self.setSettingActionValue(self.threeCB, self.threeOB, person.Three)
        except KeyError:
            self.setting.add(person_name)
            self.setupUserSetting(person_name)
        except (IndexError, AttributeError):
            self.setting.resetToDefault(person_name)
            self.setupUserSetting(person_name)

    def setSettingActionValue(self, cb, field, value):
        options = value.split(",")
        action = options[0]
        other = options[1]
        if action == "L":
            cb.setCurrentIndex(0)
        elif action == "R":
            cb.setCurrentIndex(1)
        elif action == "U":
            cb.setCurrentIndex(2)
        elif action == "D":
            cb.setCurrentIndex(3)
        elif action == "O":
            cb.setCurrentIndex(4)

        field.setText(other)

    def setupSetting(self):
        self.personWidget.clear()
        for key in self.setting.user.keys():
            self.personWidget.addItem(key)

        self.personWidget.setCurrentRow(0)

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

    def onSettingValueChanged(self, CB, LE, attrType):
        name = self.personWidget.currentItem().text()
        action = ""
        if CB.currentIndex() == 0:
            action = "L"
        elif CB.currentIndex() == 1:
            action = "R"
        elif CB.currentIndex() == 2:
            action = "U"
        elif CB.currentIndex() == 3:
            action = "D"
        elif CB.currentIndex() == 4:
            action = "O"

        other = LE.text()

        setattr(self.setting.user[name], attrType, f"{action},{other}")

    def openFilePicker(self, LE):
        file_path, _ = QFileDialog.getOpenFileName(None, 'Choose file', '', 'All files (*.*)')
        if file_path:
            LE.setText(file_path)


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
