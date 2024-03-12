# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_spinner.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QSizePolicy, QWidget)

class Ui_Spinner(object):
    def setupUi(self, Spinner):
        if not Spinner.objectName():
            Spinner.setObjectName(u"Spinner")
        Spinner.resize(297, 220)
        self.centralwidget = QWidget(Spinner)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        self.centralwidget.setFont(font)
        self.circularProgressBar = QFrame(self.centralwidget)
        self.circularProgressBar.setObjectName(u"circularProgressBar")
        self.circularProgressBar.setGeometry(QRect(10, 10, 200, 200))
        self.circularProgressBar.setFont(font)
        self.circularProgressBar.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBar)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 180, 180))
        self.circularProgress.setStyleSheet(u"QFrame {\n"
"	border-radius: 90px;\n"
"	background-color: rgb(153, 204, 255);\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.circularProgress)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(10, 10, 160, 160))
        self.circularContainer.setStyleSheet(u"QFrame {\n"
"	border-radius: 80px;\n"
"	background-color: rgb(56, 58, 89);\n"
"}")
        self.circularContainer.setFrameShape(QFrame.NoFrame)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.loadingLabel = QLabel(self.circularContainer)
        self.loadingLabel.setObjectName(u"loadingLabel")
        self.loadingLabel.setGeometry(QRect(20, 60, 115, 33))
        self.loadingLabel.setFont(font)
        self.loadingLabel.setStyleSheet(u"color: rgb(153, 204, 255);\n"
"font-size: 20px;")
        self.loadingLabel.setAlignment(Qt.AlignCenter)
        self.circularBackground = QFrame(self.circularProgressBar)
        self.circularBackground.setObjectName(u"circularBackground")
        self.circularBackground.setGeometry(QRect(10, 10, 180, 180))
        self.circularBackground.setStyleSheet(u"QFrame {\n"
"	border-radius: 90px;\n"
"	background-color: rgba(43, 44, 52, 120);\n"
"}")
        self.circularBackground.setFrameShape(QFrame.StyledPanel)
        self.circularBackground.setFrameShadow(QFrame.Raised)
        self.circularBackground.raise_()
        self.circularProgress.raise_()
        Spinner.setCentralWidget(self.centralwidget)

        self.retranslateUi(Spinner)

        QMetaObject.connectSlotsByName(Spinner)
    # setupUi

    def retranslateUi(self, Spinner):
        Spinner.setWindowTitle(QCoreApplication.translate("Spinner", u"MainWindow", None))
        self.loadingLabel.setText(QCoreApplication.translate("Spinner", u"Обработка...", None))
    # retranslateUi

