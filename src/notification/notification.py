from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6 import QtCore
from UI.notification import Ui_Notification
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QPainter, QFontMetrics
from PySide6.QtCore import Qt, QSize


class Notification(QWidget):
    def __init__(self, notification, notification_type):
        super().__init__()

        self.setWindowFlag(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui = Ui_Notification()
        self.ui.setupUi(self)

        svg_path = u":/svg/check.svg" if notification_type else u":/svg/cross-circle.svg"
        self.ui.svg_label.setPixmap(QPixmap(svg_path))
        self.ui.notification_message_label.setText(notification)

        QtCore.QTimer.singleShot(4000, self.close)
