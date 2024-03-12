import sys
import os
import inspect
from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from PySide6 import QtCore
from src.entrance.entrance import EntranceWindow
from UI.load_splash_screen import Ui_SplashScreen

cmd_main = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))
if cmd_main not in sys.path:
    sys.path.insert(0, cmd_main)

workdir = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(
    inspect.currentframe()))[0], "../../../")))


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        self.value = 0
        self.entrance = None

    def progress(self):
        self.ui.progressBar.setValue(self.value)
        if self.value >= 100:
            self.timer.stop()
            self.entrance = EntranceWindow()
            self.entrance.show()
            self.close()
        self.value += 1


if __name__ == "__main__":
    app = QApplication()
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())
