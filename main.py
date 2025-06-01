# Import modules
import sys

from mod.log import get_logger
from PySide6.QtWidgets import QMainWindow, QApplication, QStackedWidget, QWidget, QGridLayout

# Import own modules
from config import Logconfig, User_data
from mod.ui_main_window import Ui_MainWindow
from mod.ui_install import Ui_Form

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

        # Labels
        self.ui.lbl_Title.setText(f"{APP_NAME} V{VERSION}")


        # Add screens to stackedwidget
        # Voeg de QStackedWidget toe aan de widget_stack en geef het een layout
        self.stacked_widget = QStackedWidget()
        layout = QGridLayout(self.ui.widget_stack)
        layout.setContentsMargins(0, 0, 0, 0)  # Zodat hij netjes vult
        layout.addWidget(self.stacked_widget)

        # Widget screens
        self.empty_screen = QWidget()
        self.stacked_widget.addWidget(self.empty_screen)

        # Install screen
        self.install_screen = Install_screen()
        self.stacked_widget.addWidget(self.install_screen)

        # Butttons and actions
        self.ui.pushButton_Installer.clicked.connect(lambda: self.switch_screens(self.install_screen))


    def switch_screens(self, screen_name):
        """ Show a other screen."""
        self.stacked_widget.setCurrentWidget(screen_name)

class Install_screen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui= Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    logger.info("Applicatie opgestart")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())