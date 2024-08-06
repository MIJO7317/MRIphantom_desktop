# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_summary_screen.ui'
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

class Ui_ImporterSummaryScreen(object):
    def setupUi(self, ImporterSummaryScreen):
        if not ImporterSummaryScreen.objectName():
            ImporterSummaryScreen.setObjectName(u"ImporterSummaryScreen")
        ImporterSummaryScreen.resize(500, 350)
        ImporterSummaryScreen.setMinimumSize(QSize(500, 350))
        ImporterSummaryScreen.setMaximumSize(QSize(500, 350))
        ImporterSummaryScreen.setBaseSize(QSize(500, 350))
        self.horizontalLayoutWidget = QWidget(ImporterSummaryScreen)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(160, 290, 330, 51))
        self.navigateLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.navigateLayout.setObjectName(u"navigateLayout")
        self.navigateLayout.setContentsMargins(0, 0, 0, 0)
        self.backButton = QPushButton(self.horizontalLayoutWidget)
        self.backButton.setObjectName(u"backButton")

        self.navigateLayout.addWidget(self.backButton)

        self.importButton = QPushButton(self.horizontalLayoutWidget)
        self.importButton.setObjectName(u"importButton")

        self.navigateLayout.addWidget(self.importButton)

        self.cancelButton = QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.navigateLayout.addWidget(self.cancelButton)

        self.labelTitle = QLabel(ImporterSummaryScreen)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(10, 10, 471, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.labelTitle.setFont(font)
        self.summaryTableWidget = QTableWidget(ImporterSummaryScreen)
        self.summaryTableWidget.setObjectName(u"summaryTableWidget")
        self.summaryTableWidget.setGeometry(QRect(10, 40, 481, 251))

        self.retranslateUi(ImporterSummaryScreen)

        QMetaObject.connectSlotsByName(ImporterSummaryScreen)
    # setupUi

    def retranslateUi(self, ImporterSummaryScreen):
        ImporterSummaryScreen.setWindowTitle(QCoreApplication.translate("ImporterSummaryScreen", u"Import DICOM", None))
        self.backButton.setText(QCoreApplication.translate("ImporterSummaryScreen", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.importButton.setText(QCoreApplication.translate("ImporterSummaryScreen", u"\u0418\u043c\u043f\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.cancelButton.setText(QCoreApplication.translate("ImporterSummaryScreen", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.labelTitle.setText(QCoreApplication.translate("ImporterSummaryScreen", u"3/3 \u041a\u0440\u0430\u0442\u043a\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0438", None))
    # retranslateUi

