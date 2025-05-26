# Configuration file

# Import modules
import toml

# Modules config
from mod.log import get_logger
logger = get_logger("./log", "app.log")

class Logconfig():
    def __init__(self):
        self.log_path = "./log"
        self.log_file ="app.log"
        self.database_log_file = "database.log"


class User_data():
    def __init__(self):
        self.module_path = ""
        self.module_name = ""
        self.project_folder = ""
        self.virtualisation_soft = "" # UV, python.
        self.installed_packages = {}

    def reset_data(self):
        self.module_path = ""
        self.module_name = ""
        self.project_folder = ""
        self.virtualisation_soft = ""
        self.installed_packages = {}

class Application_info():
    """Managed the application information like name and version."""
    def __init__(self, config_file = "pyproject.toml"):  # The _ means it is a private function in this class
        self.config_file = config_file
        self._load_info()

    def _load_info(self):
        """Load the application data from the toml file."""
        try:
            data = toml.load(self.config_file)
            self.name = data["project"]["name"]
            self.version = data["project"]["version"]
            self.description = data["project"]["description"]

        except Exception as e:
            logger.error(f"Fout bij het laden van {self.config_file}: {e}")
    
    def __str__(self):
        logger.info(f"Information {self.name} v{self.version} - {self.description} loaded")
        return f"{self.name} v{self.version} - {self.description}"
    
    """ Use:
            app_info = Application_info()
            version = app_info.version
            app_name = app_info.name
            app_description = app_info.description
            for all print(app_info)"""