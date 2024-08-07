# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
        MainWindow.resize(1470, 746)
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
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mainLabel = QLabel(self.frame)
        self.mainLabel.setObjectName(u"mainLabel")
        self.mainLabel.setStyleSheet(u"color: rgb(56, 58, 89);	\n"
"font: 20pt \"Segoe UI\";\n"
"background-color: transparent;\n"
"font-size: 26px;")

        self.horizontalLayout_5.addWidget(self.mainLabel)

        self.settings_button = QPushButton(self.frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setEnabled(True)
        self.settings_button.setMinimumSize(QSize(250, 35))
        self.settings_button.setMaximumSize(QSize(250, 35))
        font = QFont()
        font.setFamilies([u"Impact"])
        font.setBold(False)
        self.settings_button.setFont(font)
        self.settings_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.settings_button)

        self.history_button = QPushButton(self.frame)
        self.history_button.setObjectName(u"history_button")
        self.history_button.setMinimumSize(QSize(250, 35))
        self.history_button.setMaximumSize(QSize(250, 35))
        font1 = QFont()
        font1.setFamilies([u"Impact"])
        font1.setBold(False)
        font1.setKerning(True)
        self.history_button.setFont(font1)
        self.history_button.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.history_button)


        self.horizontalLayout_4.addWidget(self.frame)


        self.horizontalLayout_3.addWidget(self.header)


        self.verticalLayout_8.addWidget(self.header_frame)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        self.body_frame.setEnabled(True)
        self.body_frame.setMaximumSize(QSize(16777215, 16777215))
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.moving_frame = QFrame(self.body_frame)
        self.moving_frame.setObjectName(u"moving_frame")
        self.moving_frame.setFrameShape(QFrame.Panel)

        self.horizontalLayout.addWidget(self.moving_frame)

        self.fixed_frame = QFrame(self.body_frame)
        self.fixed_frame.setObjectName(u"fixed_frame")
        self.fixed_frame.setFocusPolicy(Qt.NoFocus)
        self.fixed_frame.setStyleSheet(u"")
        self.fixed_frame.setFrameShape(QFrame.Panel)
        self.fixed_frame.setFrameShadow(QFrame.Plain)
        self.fixed_frame.setLineWidth(1)
        self.fixed_frame.setMidLineWidth(0)

        self.horizontalLayout.addWidget(self.fixed_frame)

        self.info_layout = QFrame(self.body_frame)
        self.info_layout.setObjectName(u"info_layout")
        self.info_layout.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_layout.sizePolicy().hasHeightForWidth())
        self.info_layout.setSizePolicy(sizePolicy)
        self.info_layout.setMaximumSize(QSize(300, 5000))
        self.info_layout.setFrameShape(QFrame.NoFrame)
        self.info_layout.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.info_layout)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.study_frame = QFrame(self.info_layout)
        self.study_frame.setObjectName(u"study_frame")
        self.study_frame.setEnabled(True)
        self.study_frame.setMinimumSize(QSize(300, 380))
        self.study_frame.setMaximumSize(QSize(300, 380))
        self.study_frame.setFrameShape(QFrame.NoFrame)
        self.study_frame.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.study_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_2.setContentsMargins(5, 5, 10, 5)
        self.studyData = QLabel(self.study_frame)
        self.studyData.setObjectName(u"studyData")
        self.studyData.setMaximumSize(QSize(16777215, 30))
        self.studyData.setStyleSheet(u"")
        self.studyData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.studyData)

        self.titleEdit = QLineEdit(self.study_frame)
        self.titleEdit.setObjectName(u"titleEdit")
        self.titleEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.titleEdit)

        self.descriptionEdit = QLineEdit(self.study_frame)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.descriptionEdit)

        self.fixedinfo_frame = QFrame(self.study_frame)
        self.fixedinfo_frame.setObjectName(u"fixedinfo_frame")
        self.fixedinfo_frame.setFrameShape(QFrame.StyledPanel)
        self.fixedinfo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.fixedinfo_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fixedinfo_label = QLabel(self.fixedinfo_frame)
        self.fixedinfo_label.setObjectName(u"fixedinfo_label")

        self.horizontalLayout_2.addWidget(self.fixedinfo_label)

        self.fixedimgEdit = QLineEdit(self.fixedinfo_frame)
        self.fixedimgEdit.setObjectName(u"fixedimgEdit")
        self.fixedimgEdit.setMinimumSize(QSize(0, 34))
        self.fixedimgEdit.setMaximumSize(QSize(250, 16777215))
        self.fixedimgEdit.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.fixedimgEdit)


        self.verticalLayout_2.addWidget(self.fixedinfo_frame)

        self.movinginfo_frame = QFrame(self.study_frame)
        self.movinginfo_frame.setObjectName(u"movinginfo_frame")
        self.movinginfo_frame.setFrameShape(QFrame.StyledPanel)
        self.movinginfo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.movinginfo_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.movinginfo_label = QLabel(self.movinginfo_frame)
        self.movinginfo_label.setObjectName(u"movinginfo_label")

        self.horizontalLayout_6.addWidget(self.movinginfo_label)

        self.movingimgEdit = QLineEdit(self.movinginfo_frame)
        self.movingimgEdit.setObjectName(u"movingimgEdit")
        self.movingimgEdit.setEnabled(True)
        self.movingimgEdit.setMinimumSize(QSize(0, 34))
        self.movingimgEdit.setMaximumSize(QSize(250, 16777215))
        self.movingimgEdit.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.movingimgEdit)


        self.verticalLayout_2.addWidget(self.movinginfo_frame)

        self.phantomTypeCombo = QComboBox(self.study_frame)
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

        self.registrationButton = QPushButton(self.study_frame)
        self.registrationButton.setObjectName(u"registrationButton")
        self.registrationButton.setMinimumSize(QSize(0, 34))
        self.registrationButton.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.registrationButton)

        self.interpolateButton = QCheckBox(self.study_frame)
        self.interpolateButton.setObjectName(u"interpolateButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.interpolateButton.sizePolicy().hasHeightForWidth())
        self.interpolateButton.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 127, 132, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(255, 63, 70, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(127, 0, 4, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(170, 0, 5, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush6 = QBrush(QColor(255, 127, 131, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush6)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 127))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush9 = QBrush(QColor(255, 0, 8, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush10 = QBrush(QColor(127, 0, 4, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        brush11 = QBrush(QColor(255, 76, 82, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.interpolateButton.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(10)
        font2.setBold(False)
        self.interpolateButton.setFont(font2)

        self.verticalLayout_2.addWidget(self.interpolateButton)

        self.geometryButton = QCheckBox(self.study_frame)
        self.geometryButton.setObjectName(u"geometryButton")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush12 = QBrush(QColor(255, 127, 127, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush12)
        brush13 = QBrush(QColor(255, 63, 63, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(127, 0, 0, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(170, 0, 0, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush12)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush16 = QBrush(QColor(255, 0, 0, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush17 = QBrush(QColor(127, 0, 0, 127))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        brush18 = QBrush(QColor(255, 76, 76, 255))
        brush18.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush18)
        self.geometryButton.setPalette(palette1)

        self.verticalLayout_2.addWidget(self.geometryButton)

        self.analyzeButton = QPushButton(self.study_frame)
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


        self.verticalLayout.addWidget(self.study_frame)

        self.controls_frame = QFrame(self.info_layout)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(0, 150))
        self.controls_frame.setMaximumSize(QSize(300, 16777215))
        self.controls_layout = QVBoxLayout(self.controls_frame)
        self.controls_layout.setObjectName(u"controls_layout")
        self.controls_layout.setContentsMargins(-1, 225, -1, -1)
        self.statusLabel = QLabel(self.controls_frame)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(280, 30))
        self.statusLabel.setMaximumSize(QSize(300, 30))
        self.statusLabel.setStyleSheet(u"")

        self.controls_layout.addWidget(self.statusLabel)


        self.verticalLayout.addWidget(self.controls_frame)


        self.horizontalLayout.addWidget(self.info_layout)


        self.verticalLayout_8.addWidget(self.body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MRIphantom", None))
        self.mainLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:700;\">MRI</span><span style=\" font-size:26pt;\">phantom</span></p></body></html>", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.history_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u044b\u0435 \u0442\u0435\u0441\u0442\u044b", None))
        self.studyData.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0414\u0430\u043d\u043d\u044b\u0435 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f</p></body></html>", None))
        self.titleEdit.setText("")
        self.descriptionEdit.setText("")
        self.fixedinfo_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0422", None))
        self.fixedimgEdit.setText("")
        self.movinginfo_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0420\u0422", None))
        self.movingimgEdit.setText("")
        self.phantomTypeCombo.setCurrentText("")
        self.registrationButton.setText(QCoreApplication.translate("MainWindow", u" \u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.interpolateButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c \u0438\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446\u0438\u044e", None))
        self.geometryButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043e\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.analyzeButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u043e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0439", None))
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
    # retranslateUi

