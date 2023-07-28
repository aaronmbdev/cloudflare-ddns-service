import json
import logging
import os


class DDNSSetup:
    def __init__(self) -> None:
        self.DEFAULT_PATH = "config"
        self.DEFAULT_FILENAME = "config.json"
        self.logger = logging.getLogger("ddns")
        self.logger.info("Starting DDNS setup")

    def setup_ddns_service(self, args) -> None:

        if not os.path.exists(self.DEFAULT_PATH):
            self.logger.info("Config folder does not exists. Creating one...")
            os.makedirs(self.DEFAULT_PATH)
        else:
            self.logger.info("Config folder already exists")

        full_path = f"{self.DEFAULT_PATH}/{self.DEFAULT_FILENAME}"
        if os.path.exists(full_path):
            self.logger.warn("A config file already exists but it will be replaced with the latest information")

        data = {
            "cloudflare_token": args.cloudflare_token,
            "domain" : args.domain,
            "subdomains": [
                {
                    "name": args.subdomain,
                    "proxy": False if args.no_proxy else True
                }
            ]
        }

        json_str = json.dumps(data, indent=4)

        with open(full_path, "w") as file:
            file.write(json_str)

        self.logger.info("Config file created successfully")
