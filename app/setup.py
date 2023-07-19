import logging
import os


class DDNSSetup:
    def __init__(self) -> None:
        logging.info("Starting DDNS setup")
        self.DEFAULT_PATH = "config"
        self.DEFAULT_FILENAME = "config.json"

    def setup_ddns_service(self, args) -> None:

        if not os.path.exists(self.DEFAULT_PATH):
            logging.info("Config folder does not exists. Creating one...")
            os.makedirs(self.DEFAULT_PATH)
        else:
            logging.info("Config folder already exists")

        full_path = f"{self.DEFAULT_PATH}/{self.DEFAULT_FILENAME}"
        if os.path.exists(full_path):
            logging.warn("A config file already exists but it will be replaced with the latest information")