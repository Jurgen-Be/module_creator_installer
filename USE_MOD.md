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
-   Logconfig
    """ This submodule is for the path en filenames of the logging. """
    Use:
        logconfig = Logconfig()
        for the logging path logconfig.log_path
        for the logging filename logconfig.log_file
        for the database logging logconfig.database_log_file

-   User_data
    """ This submodule is for the data of the user. """
    Use:
        userdata = User_data()
        options module_path, module_name, project_folder, virtualisation_soft, installed_packages

        var_name = userdata.option

        Reset the data:
        reset_data = userdata.reset_data()