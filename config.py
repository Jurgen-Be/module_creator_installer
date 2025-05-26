# Configuration file

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