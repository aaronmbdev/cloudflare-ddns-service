
from json import JSONDecodeError
import logging
from services.cloudflare_service import CloudflareService

from services.config_reader import ConfigReader


class DDNSStart:
    def __init__(self) -> None:
        self.logger = logging.getLogger("ddns")
        self.logger.info("Starting DDNS Service")
        self.cloudflare = CloudflareService(ConfigReader().read_config())

    def launch(self) -> None:
        self.logger.info("test")
        