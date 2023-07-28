
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

    def __launch_service__(self):
        while True:
            all_records = self.cloudflare.get_subdomain_records()
            records_to_update = self.cloudflare.records_to_update(all_records)
            current_ip = self.ip_retriever.find()

            for record in records_to_update:
                record_id = record["id"]
                subdomain = record["name"]
                record_value = record["content"]
                self.logger.info(f"The IP Address for {subdomain} changed. {current_ip} != {record_value}. Update in progress")
                self.cloudflare.update_subdomain_record(current_ip, record_id, subdomain)
                self.logger.info("Value updated in Cloudflare successfully")
            time.sleep(600)


    def launch(self) -> None:
        self.logger.info("Started DDNS Service successfully")
        thread = threading.Thread(target=self.__launch_service__)
        thread.start()
