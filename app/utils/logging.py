import logging.config
import logging.handlers
import sys

class LoggingManager:
    def __init__(self) -> None:
        self.__configure__()
        
    def __configure__(self) -> None:
        logging.basicConfig(
            stream = sys.stdout,
            level = logging.INFO,
            format = "%(levelname)s: %(asctime)s - %(message)s"
        )

