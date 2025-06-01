# Import modules
import sys

from mod.log import get_logger
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget

# Import own modules
from config import Logconfig, User_data
from mod.ui_main_window import Ui_MainWindow

VERSION = "0.0.2"
APP_NAME = "Python Manager"

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

        # Config stacked widget frame
        self.stacked_widget = QStackedWidget(self.ui.widget)

        # Labels
        self.ui.lbl_Title.setText(f"{APP_NAME} V{VERSION}")

        # Butttons and actions
        self.ui.pushButton_Installer.clicked.connect() # Lambda nog invoegen

        # Widget screens

            # Install screen
        self.install_screen = "" # Nog invullen na creeren ui file

        # Add screens to stackedwidget
        self.stacked_widget.addWidget(self.install_screen)

    def switch_screens(self, screen_name):
        """ Show a other screen."""
        self.stacked_widget.setCurrentWidget(screen_name)

if __name__ == "__main__":
    logger.info("Applicatie opgestart")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())