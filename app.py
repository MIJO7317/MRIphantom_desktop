import os
import sys
import inspect
from PySide6 import QtGui
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from src.splash_screen.splash_screen import SplashScreen

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

try:
    from ctypes import windll
    app_id = 'MRIphantom.0.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling)
    app.setWindowIcon(QtGui.QIcon("./assets/icons/MRIphantom_icon.ico"))
    preload = SplashScreen()
    preload.show()
    sys.exit(app.exec())
