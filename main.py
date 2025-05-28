# Import modules
from mod.log import get_logger

# Import own modules
from config import Logconfig, User_data

VERSION = "0.0.2"

# Modules config
logconfig = Logconfig()
user_data = User_data()
logger = get_logger(logconfig.log_path, logconfig.log_file)    # Algemene logger
database_logger = get_logger(logconfig.log_path, logconfig.database_log_file)  # Logger voor database logging

def main():
    pass


if __name__ == "__main__":
    logger.info("Applicatie opgestart")
    main()
