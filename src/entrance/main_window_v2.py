import os
import sys
import inspect
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PySide6.QtCore import (
    Signal
)



workdir = os.path.realpath(
    os.path.abspath(
        os.path.join(
            os.path.split(inspect.getfile(inspect.currentframe()))[0], "../../"
        )
    )
)


class EntranceWindow(QMainWindow):
    send_shift = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()

    def initUi(self):
        self.vbox = QVBoxLayout()
        self.setLayout(self.vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    entrance = EntranceWindow()
    entrance.show()
    sys.exit(app.exec())
