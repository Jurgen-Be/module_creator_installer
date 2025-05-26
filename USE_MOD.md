# How to use the modules

## Module log.py
The module is useful for logging information, problems, ... to a log file.

-   Import the module: from mod.log import get_logger
-   Assign the log module:  logger = get_logger("dir_path", "filename")
-   Log messages:
    -   info message: logger.info("message)
    -   debug message: logger.debug ("message")
    -   warning message: logger.warning("message")
    -   error message: logger.error("message")
    -   critical message: logger.critical("message")

## Module config.py
