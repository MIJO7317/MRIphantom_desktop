# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_select_screen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_ImporterSelectScreen(object):
    def setupUi(self, ImporterSelectScreen):
        if not ImporterSelectScreen.objectName():
            ImporterSelectScreen.setObjectName(u"ImporterSelectScreen")
        ImporterSelectScreen.resize(500, 350)
        ImporterSelectScreen.setMinimumSize(QSize(500, 350))
        ImporterSelectScreen.setMaximumSize(QSize(500, 350))
        ImporterSelectScreen.setBaseSize(QSize(500, 350))
        self.horizontalLayoutWidget = QWidget(ImporterSelectScreen)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(160, 290, 330, 51))
        self.navigateLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.navigateLayout.setObjectName(u"navigateLayout")
        self.navigateLayout.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.horizontalLayoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.navigateLayout.addWidget(self.backButton)

        self.forwardButton = QPushButton(self.horizontalLayoutWidget)
        self.forwardButton.setObjectName(u"forwardButton")

        self.navigateLayout.addWidget(self.forwardButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.navigateLayout.addWidget(self.cancelButton)

        self.labelTitle = QLabel(ImporterSelectScreen)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(10, 10, 231, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.labelTitle.setFont(font)
        self.tableWidget = QTableWidget(ImporterSelectScreen)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 481, 251))

        self.retranslateUi(ImporterSelectScreen)

        QMetaObject.connectSlotsByName(ImporterSelectScreen)
    # setupUi

    def retranslateUi(self, ImporterSelectScreen):
        ImporterSelectScreen.setWindowTitle(QCoreApplication.translate("ImporterSelectScreen", u"Import DICOM", None))
        self.backButton.setText(QCoreApplication.translate("ImporterSelectScreen", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.forwardButton.setText(QCoreApplication.translate("ImporterSelectScreen", u"\u0414\u0430\u043b\u0435\u0435", None))
        self.cancelButton.setText(QCoreApplication.translate("ImporterSelectScreen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.labelTitle.setText(QCoreApplication.translate("ImporterSelectScreen", u"2/3 \u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
    # retranslateUi

