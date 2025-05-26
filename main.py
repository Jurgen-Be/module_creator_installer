# Import modules
from mod.log import get_logger

# Import eigen modules
from config import Logconfig

# Modules aanroepen
logconfig = Logconfig()
logger = get_logger(logconfig.log_path, logconfig.log_file)    # Algemene logger
database_logger = get_logger(logconfig.log_path, logconfig.database_log_file)  # Logger voor database logging


def main():
    pass


if __name__ == "__main__":
    logger.info("Applicatie opgestart")
    main()
