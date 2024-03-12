import os
import sys
import inspect

from PySide6.QtWidgets import QMainWindow, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from PySide6 import QtCore
from UI.ui_spinner import Ui_Spinner

cmd_main = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))
if cmd_main not in sys.path:
    sys.path.insert(0, cmd_main)


class Spinner(QMainWindow):
    """
    The spinner
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_Spinner()
        self.ui.setupUi(self)

        self.value = 0
        self.progress_bar_value(0)
        self.entrance = None

        self.setWindowFlag(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBackground.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(20)

    def progress(self):
        """

        """
        if self.value >= 100:
            self.value = 1

        self.progress_bar_value(self.value)

        self.value += 1
        self.ui.loadingLabel.setText("Обработка.")
        if 33 <= self.value <= 67:
            self.ui.loadingLabel.setText("Обработка..")
        if self.value > 67:
            self.ui.loadingLabel.setText("Обработка...")

    def progress_bar_value(self, value):
        """
        The progress bar
        """

        style_sheet = """
        QFrame {
            border-radius: 90px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{first_stop} rgba(170, 0, 255, 0),
            stop:{second_stop} rgb(153, 204, 255));
        }
        """

        progress = (100 - value) / 100.0

        first_stop = str(progress - 0.001)
        second_stop = str(progress)

        new_style_sheet = style_sheet.replace(
            "{first_stop}", first_stop).replace(
            "{second_stop}", second_stop)

        self.ui.circularProgress.setStyleSheet(new_style_sheet)
