# Import modules
import sys

from mod.log import get_logger
from PySide6.QtWidgets import QMainWindow, QApplication

# Import own modules
from config import Logconfig, User_data
from mod.ui_main_window import Ui_MainWindow

VERSION = "0.0.2"

# Modules config
logconfig = Logconfig()
user_data = User_data()
logger = get_logger(logconfig.log_path, logconfig.log_file)    # Algemene logger
database_logger = get_logger(logconfig.log_path, logconfig.database_log_file)  # Logger voor database logging

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        logger.info("GUI started")


if __name__ == "__main__":
    logger.info("Applicatie opgestart")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())