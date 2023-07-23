
import logging
import threading
import time
from app.services.cloudflare_service import CloudflareService

from app.services.config_reader import ConfigReader
from app.services.ip_retriever import IPRetriever


class DDNSStart:
    def __init__(self, args) -> None:
        self.logger = logging.getLogger("ddns")
        self.logger.info("Starting DDNS Service")
        self.cloudflare = CloudflareService(ConfigReader().read_config())
        self.ip_retriever = IPRetriever()
        self.proxy = False if args.no_proxy else True

    def __launch_service__(self):
        while True:
            records = self.cloudflare.get_subdomain_records()
            current_ip = self.ip_retriever.find()

            if records is None:
                raise ValueError("There was an error trying to retrieve the DNS values of the subdomain")
            
            if records["value"] != current_ip:
                self.logger.info("The IP Address has changed and is not equal to the DNS record. Updating...")
                self.cloudflare.update_subdomain_record(current_ip, records["id"], self.proxy)
                self.logger.info("Value updated in Cloudflare successfully")
            else:
                self.logger.info("The IP Adress is equal to the value of the DNS record. No changes are required")
            
            time.sleep(600)


    def launch(self) -> None:
        self.logger.info("Started DDNS Service successfully")
        thread = threading.Thread(target=self.__launch_service__)
        thread.start()
