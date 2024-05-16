# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_main_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ImporterMainScreen(object):
    def setupUi(self, ImporterMainScreen):
        if not ImporterMainScreen.objectName():
            ImporterMainScreen.setObjectName(u"ImporterMainScreen")
        ImporterMainScreen.resize(500, 350)
        ImporterMainScreen.setMinimumSize(QSize(500, 350))
        ImporterMainScreen.setMaximumSize(QSize(500, 350))
        ImporterMainScreen.setBaseSize(QSize(500, 350))
        self.horizontalLayoutWidget = QWidget(ImporterMainScreen)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(160, 290, 330, 51))
        self.navigateLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.navigateLayout.setObjectName(u"navigateLayout")
        self.navigateLayout.setContentsMargins(0, 0, 0, 0)
        self.forwardButton = QPushButton(self.horizontalLayoutWidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.navigateLayout.addWidget(self.forwardButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.navigateLayout.addWidget(self.cancelButton)

        self.labelTitle = QLabel(ImporterMainScreen)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(10, 10, 231, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.labelTitle.setFont(font)
        self.verticalLayoutWidget = QWidget(ImporterMainScreen)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 50, 481, 81))
        self.filebrowseLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.filebrowseLayout.setObjectName(u"filebrowseLayout")
        self.filebrowseLayout.setContentsMargins(0, 0, 0, 0)
        self.infoLabel = QLabel(self.verticalLayoutWidget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setMinimumSize(QSize(0, 20))
        self.infoLabel.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.infoLabel.setFont(font1)

        self.filebrowseLayout.addWidget(self.infoLabel)

        self.pathLayout = QHBoxLayout()
        self.pathLayout.setObjectName(u"pathLayout")
        self.filepathLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.filepathLineEdit.setObjectName(u"filepathLineEdit")
        self.filepathLineEdit.setMinimumSize(QSize(200, 30))
        self.filepathLineEdit.setMaximumSize(QSize(500, 30))

        self.pathLayout.addWidget(self.filepathLineEdit)

        self.browseButton = QPushButton(self.verticalLayoutWidget)
        self.browseButton.setObjectName(u"browseButton")

        self.pathLayout.addWidget(self.browseButton)


        self.filebrowseLayout.addLayout(self.pathLayout)

        self.verticalLayoutWidget_2 = QWidget(ImporterMainScreen)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 150, 191, 71))
        self.datatypeLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.datatypeLayout.setObjectName(u"datatypeLayout")
        self.datatypeLayout.setContentsMargins(0, 0, 0, 0)
        self.typeInfoLabel = QLabel(self.verticalLayoutWidget_2)
        self.typeInfoLabel.setObjectName(u"typeInfoLabel")

        self.datatypeLayout.addWidget(self.typeInfoLabel)

        self.dataComboBox = QComboBox(self.verticalLayoutWidget_2)
        self.dataComboBox.setObjectName(u"dataComboBox")

        self.datatypeLayout.addWidget(self.dataComboBox)


        self.retranslateUi(ImporterMainScreen)

        QMetaObject.connectSlotsByName(ImporterMainScreen)
    # setupUi

    def retranslateUi(self, ImporterMainScreen):
        ImporterMainScreen.setWindowTitle(QCoreApplication.translate("ImporterMainScreen", u"Import DICOM", None))
        self.forwardButton.setText(QCoreApplication.translate("ImporterMainScreen", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.cancelButton.setText(QCoreApplication.translate("ImporterMainScreen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.labelTitle.setText(QCoreApplication.translate("ImporterMainScreen", u"1/3 \u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.infoLabel.setText(QCoreApplication.translate("ImporterMainScreen", u"\u0424\u0430\u0439\u043b \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f:", None))
        self.browseButton.setText(QCoreApplication.translate("ImporterMainScreen", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.typeInfoLabel.setText(QCoreApplication.translate("ImporterMainScreen", u"\u0422\u0438\u043f \u0434\u0430\u043d\u043d\u044b\u0445", None))
    # retranslateUi

