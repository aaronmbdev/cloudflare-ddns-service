import json
import logging
import os

class ConfigReader:
    def __init__(self) -> None:
        self.CONFIG_PATH = "config/config.json"
        self.logger = logging.getLogger("ddns")
        self.required_keys = {"cloudflare_token", "domain", "subdomains"}

    def read_config(self) -> dict:
        self.logger.info("Reading configuration file")
        if not os.path.exists(self.CONFIG_PATH):
            raise IOError("There's no config file available. File not found.")
        
        config_contents = None
        with open(self.CONFIG_PATH) as file:
            config_contents = file.read()
        
        try:
            data = json.loads(config_contents)
            data_keys = set(data.keys())
        except json.JSONDecodeError:
            raise ValueError("The configuration file is not a valid JSON. Check the schema")

        missing = self.required_keys - data_keys
        if len(missing) != 0:
            raise ValueError(
                f"The configuration file is missing required keys. The following kets are missing: {missing}")
        
        self.logger.info("Configuration found and loaded successfully")
        return data
        