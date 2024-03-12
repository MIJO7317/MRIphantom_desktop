# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notification.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_rc

class Ui_Notification(object):
    def setupUi(self, Notification):
        if not Notification.objectName():
            Notification.setObjectName(u"Notification")
        Notification.resize(392, 55)
        Notification.setStyleSheet(u"background-color: white;\n"
"font-family: Montserrat;\n"
"color: white;")
        self.verticalLayout = QVBoxLayout(Notification)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(Notification)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.svg_frame = QFrame(self.main_frame)
        self.svg_frame.setObjectName(u"svg_frame")
        self.svg_frame.setMaximumSize(QSize(50, 50))
        self.svg_frame.setFrameShape(QFrame.StyledPanel)
        self.svg_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.svg_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.svg_label = QLabel(self.svg_frame)
        self.svg_label.setObjectName(u"svg_label")
        self.svg_label.setMaximumSize(QSize(35, 35))
        self.svg_label.setStyleSheet(u"color: #6246EA;")
        self.svg_label.setPixmap(QPixmap(u":/svg/cross-circle.svg"))
        self.svg_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.svg_label)


        self.horizontalLayout.addWidget(self.svg_frame)

        self.text_frame = QFrame(self.main_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.notification_message_label = QLabel(self.text_frame)
        self.notification_message_label.setObjectName(u"notification_message_label")
        self.notification_message_label.setMaximumSize(QSize(16777215, 40))
        self.notification_message_label.setLayoutDirection(Qt.LeftToRight)
        self.notification_message_label.setStyleSheet(u"color: black;\n"
"font-size: 14px;")
        self.notification_message_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.notification_message_label)


        self.horizontalLayout.addWidget(self.text_frame)


        self.verticalLayout.addWidget(self.main_frame)


        self.retranslateUi(Notification)

        QMetaObject.connectSlotsByName(Notification)
    # setupUi

    def retranslateUi(self, Notification):
        Notification.setWindowTitle(QCoreApplication.translate("Notification", u"Form", None))
        self.svg_label.setText("")
        self.notification_message_label.setText(QCoreApplication.translate("Notification", u"\u0412\u044b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043b\u0438 \u043d\u0430\u0447\u0430\u043b\u043e \u0432\u0438\u0434\u0435\u043e\u0444\u0440\u0430\u0433\u043c\u0435\u043d\u0442\u0430!", None))
    # retranslateUi

