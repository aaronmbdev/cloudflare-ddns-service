import logging.config
import logging.handlers
import sys

class LoggingManager:
    def __init__(self) -> None:
        self.__configure__()
        
    def __configure__(self) -> None:
        logger = logging.getLogger("ddns")
        formatter = logging.Formatter(
            "[%(asctime)s][%(name)s][%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S"
        )
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.INFO)
        logger.addHandler(stream_handler)
        logger.propagate = False
        logger.setLevel(logging.INFO)
