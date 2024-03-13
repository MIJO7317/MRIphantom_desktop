# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 435)
        MainWindow.setStyleSheet(u"font-family: Montserrat;\n"
"font-weight : 400;\n"
"border-color: transparent\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"background-color: #FFFFFE;\n"
"color: rgb(43, 44, 52);\n"
"border-radius: 10px;\n"
"border: 2px solid #c5c7d4;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"color: white;\n"
"background-color: #c5c7d4;\n"
"border-radius: 10px;\n"
"border: 2px solid #c5c7d4;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgb(43, 44, 52);\n"
"background-color: #c5c7d4;\n"
"border-radius: 10px;\n"
"border: 2px solid #c5c7d4;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgb(43, 44, 52);\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: #FFFFFE;\n"
"color: rgb(43, 44, 52);\n"
"border-radius: 10px;\n"
"border: 2px solid #c5c7d4;\n"
"height: 30px;\n"
"font-size: 12px;\n"
"}\n"
"\n"
"\n"
"QWidget {\n"
"background-color: white;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(400, 0))
        self.header_frame.setMaximumSize(QSize(16777215, 80))
        self.header_frame.setStyleSheet(u"font-family: Impact;\n"
"font-weight : 400;")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.header_frame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 0))
        self.header.setStyleSheet(u"background-color: #2B2C34;\n"
"width: 2000px")
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.header.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"width: 2000px")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.mainLabel = QLabel(self.frame)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setGeometry(QRect(30, 10, 400, 51))
        self.mainLabel.setStyleSheet(u"color: rgb(56, 58, 89);	\n"
"font: 20pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"font-size: 26px;")

        self.horizontalLayout_4.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.header)


        self.verticalLayout_8.addWidget(self.header_frame)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setEnabled(True)
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.data_frame = QFrame(self.body_frame)
        self.data_frame.setObjectName(u"data_frame")
        self.data_frame.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_frame.sizePolicy().hasHeightForWidth())
        self.data_frame.setSizePolicy(sizePolicy)
        self.data_frame.setMaximumSize(QSize(370, 16777215))
        self.data_frame.setFrameShape(QFrame.NoFrame)
        self.data_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.data_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.name_frame = QFrame(self.data_frame)
        self.name_frame.setObjectName(u"name_frame")
        self.name_frame.setEnabled(True)
        self.name_frame.setMaximumSize(QSize(16777215, 370))
        self.name_frame.setFrameShape(QFrame.NoFrame)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.name_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.studyData = QLabel(self.name_frame)
        self.studyData.setObjectName(u"studyData")
        self.studyData.setMaximumSize(QSize(16777215, 30))
        self.studyData.setStyleSheet(u"")
        self.studyData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.studyData)

        self.titleEdit = QLineEdit(self.name_frame)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.titleEdit)

        self.descriptionEdit = QLineEdit(self.name_frame)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.descriptionEdit)

        self.fixedimgEdit = QLineEdit(self.name_frame)
        self.fixedimgEdit.setObjectName(u"fixedimgEdit")
        self.fixedimgEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.fixedimgEdit)

        self.movingimgEdit = QLineEdit(self.name_frame)
        self.movingimgEdit.setObjectName(u"movingimgEdit")
        self.movingimgEdit.setEnabled(True)
        self.movingimgEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.movingimgEdit)

        self.phantomTypeCombo = QComboBox(self.name_frame)
        self.phantomTypeCombo.setObjectName(u"phantomTypeCombo")
        self.phantomTypeCombo.setMinimumSize(QSize(0, 34))
        self.phantomTypeCombo.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid #9799a6;\n"
"    border-radius: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    background-color: white;\n"
" }\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(243, 244, 255);\n"
"    padding: 10px;\n"
"    border: 2px solid rgb(212, 215, 255);\n"
"    border-radius: 10px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    selection-background-color: rgb(140, 146, 255);\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"outline: 0px;\n"
"}")

        self.verticalLayout_2.addWidget(self.phantomTypeCombo)

        self.interpolateButton = QCheckBox(self.name_frame)
        self.interpolateButton.setObjectName(u"interpolateButton")

        self.verticalLayout_2.addWidget(self.interpolateButton)

        self.geometryButton = QCheckBox(self.name_frame)
        self.geometryButton.setObjectName(u"geometryButton")

        self.verticalLayout_2.addWidget(self.geometryButton)

        self.analyzeButton = QPushButton(self.name_frame)
        self.analyzeButton.setObjectName(u"analyzeButton")
        self.analyzeButton.setMinimumSize(QSize(0, 34))
        self.analyzeButton.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(0, 235, 255, 20);\n"
"color: black;\n"
"border-radius: 10px;\n"
"border: 2px solid rgba(0, 235, 255, 255);\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: white;\n"
"color: rgb(98, 70, 234);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(98, 70, 234);\n"
"font-size: 14px;\n"
"}")

        self.verticalLayout_2.addWidget(self.analyzeButton)

        self.nameVideoLabel = QLabel(self.name_frame)
        self.nameVideoLabel.setObjectName(u"nameVideoLabel")
        self.nameVideoLabel.setMaximumSize(QSize(16777215, 20))
        self.nameVideoLabel.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.nameVideoLabel)


        self.verticalLayout.addWidget(self.name_frame)


        self.horizontalLayout_2.addWidget(self.data_frame)


        self.verticalLayout_8.addWidget(self.body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MRIphantom", None))
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:700;\">MRI</span><span style=\" font-size:26pt;\">phantom</span></p></body></html>", None))
        self.studyData.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f</p></body></html>", None))
        self.titleEdit.setText("")
        self.descriptionEdit.setText("")
        self.fixedimgEdit.setText("")
        self.movingimgEdit.setText("")
        self.phantomTypeCombo.setCurrentText("")
        self.interpolateButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u043c\u0430\u0440\u043a\u0435\u0440\u043e\u0432", None))
        self.geometryButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0433\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0443\u044e \u043c\u043e\u0434\u0435\u043b\u044c \u0444\u0430\u043d\u0442\u043e\u043c\u0430", None))
        self.analyzeButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0430\u0441\u0447\u0435\u0442", None))
        self.nameVideoLabel.setText("")
    # retranslateUi

