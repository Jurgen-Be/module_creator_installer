# Logger for the project

# Import modules
import logging
from logging.handlers import RotatingFileHandler
import os

# Settings for logrotation
MAX_LOG_SIZE = 5_000_000 # Maximum size is 5MB
BACKUP_COUNT = 5         # Maximum backups is 5

# Funtions
def get_logger(directory: str, filename: str) -> logging.Logger:
    """Create and return a logger with max size and backups."""
    os.makedirs(directory, exist_ok=True)
    log_path = os.path.join(directory, filename)

    logger = logging.getLogger(filename)  # Loggger setup the logger filename
    
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)        # Logger level setup

        # Format of the log message
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Filehandler with rotation
        file_handler = RotatingFileHandler(log_path, maxBytes=MAX_LOG_SIZE, backupCount=BACKUP_COUNT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# How to use
"""
logger = get_logger("logs", "app.log")
logger.info("This is a information message")
logger.error("This is a error message")
"""