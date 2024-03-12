# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_widget_logo.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QFrame, QLabel, QWidget)
import os
import sys
import inspect
cmd_main = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))
if cmd_main not in sys.path:
    sys.path.insert(0, cmd_main)


# import resources_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(338, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamilies([u"Impact"])
        self.centralwidget.setFont(font)
        self.circularProgressBar = QFrame(self.centralwidget)
        self.circularProgressBar.setObjectName(u"circularProgressBar")
        self.circularProgressBar.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBar.setFont(font)
        self.circularProgressBar.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QFrame.Raised)
        self.circularBackground = QFrame(self.circularProgressBar)
        self.circularBackground.setObjectName(u"circularBackground")
        self.circularBackground.setGeometry(QRect(10, 10, 300, 300))
        self.circularBackground.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: rgba(43, 44, 52, 120);\n"
"}")
        self.circularBackground.setFrameShape(QFrame.StyledPanel)
        self.circularBackground.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularBackground)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(0, 0, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(170, 0, 255, 0), stop:0.750 rgba(98, 70, 234, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgress)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(10, 10, 280, 280))
        self.circularContainer.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(43, 44, 52);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.NoFrame)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.circularContainer)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 240, 240))
        self.label.setStyleSheet(u"background-color: transparent;")
        self.label.setPixmap(QPixmap(u":/svg/circle_logo.svg"))
        self.label.setScaledContents(True)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label.setText("")
    # retranslateUi

