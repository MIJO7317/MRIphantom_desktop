import os
import sys
import inspect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from src.splash_screen.splash_screen import SplashScreen
from src.entrance.entrance import EntranceWindow

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# try:
#     from ctypes import windll
#     app_id = 'MRIphantom.0.1'
#     windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
# except ImportError:
#     pass

# export DEBUG=2 in terminal to enter debug mode
debug = 0
try:
    debug = int(os.environ['DEBUG'])
except KeyError:
    print('DEBUG environment variable is not set. Please set DEBUG variable.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./assets/icons/MRIphantom_icon.ico"))
    if debug == 2:
        entrance = EntranceWindow()
        entrance.show()
    else:
        preload = SplashScreen()
        preload.show()
    sys.exit(app.exec())
