# Import modules
from mod.log import get_logger

logger = get_logger("log", "app.log")

def main():
    print("Hello from module-creator-installer!")
    logger.info("De logger werkt")


if __name__ == "__main__":
    main()
