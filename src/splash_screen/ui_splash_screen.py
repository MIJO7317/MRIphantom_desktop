# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBar = QFrame(self.centralwidget)
        self.circularProgressBar.setObjectName(u"circularProgressBar")
        self.circularProgressBar.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBar.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBar)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(170, 0, 255, 0), stop:0.750 rgba(98, 70, 234, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBackground = QFrame(self.circularProgressBar)
        self.circularBackground.setObjectName(u"circularBackground")
        self.circularBackground.setGeometry(QRect(10, 10, 300, 300))
        self.circularBackground.setStyleSheet(u"QFrame {\n"
"	border-radius: 150px;\n"
"	background-color: rgba(43, 44, 52, 120);\n"
"}")
        self.circularBackground.setFrameShape(QFrame.StyledPanel)
        self.circularBackground.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgressBar)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(25, 25, 270, 270))
        self.circularContainer.setStyleSheet(u"QFrame {\n"
"	border-radius: 135px;\n"
"	background-color: rgb(43, 44, 52);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.NoFrame)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.circularContainer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 70, 124, 122))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(30)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.loadingLabel = QLabel(self.widget)
        self.loadingLabel.setObjectName(u"loadingLabel")
        font = QFont()
        font.setFamilies([u"Impact"])
        self.loadingLabel.setFont(font)
        self.loadingLabel.setStyleSheet(u"color: white;\n"
"font-size: 26px;")
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loadingLabel, 2, 0, 1, 1)

        self.larynxLabel = QLabel(self.widget)
        self.larynxLabel.setObjectName(u"larynxLabel")
        self.larynxLabel.setFont(font)
        self.larynxLabel.setStyleSheet(u"color: white;\n"
"font-size: 46px;")
        self.larynxLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.larynxLabel, 1, 0, 1, 1)

        self.circularBackground.raise_()
        self.circularProgress.raise_()
        self.circularContainer.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.loadingLabel.setText(QCoreApplication.translate("SplashScreen", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.larynxLabel.setText(QCoreApplication.translate("SplashScreen", u"Larynx", None))
    # retranslateUi

