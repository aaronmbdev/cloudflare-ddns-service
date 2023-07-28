import logging
from typing import Any
import CloudFlare


class CloudflareService:
    def __init__(self, config: dict) -> None:
        self.logger = logging.getLogger("ddns")
        self.domain = config["domain"]
        self.subdomains = config["subdomains"]
        self.client = CloudFlare.CloudFlare(
            token=config["cloudflare_token"]
        )
        self.__verify_domain_is_ours__()
        
    def __verify_domain_is_ours__(self) -> bool:
        zones = self.client.zones.get(params={'name': self.domain})
        if not zones:
            raise ValueError(f"The domain {self.domain} was not found in the Cloudflare account")
        self.zone_id = zones[0]['id']
        self.logger.info(f"Domain found in the account with zone id '{self.zone_id}'")
        

    def get_subdomain_records(self) -> list:
        return self.client.zones.dns_records.get(self.zone_id)
    

    def records_to_update(self, records):
        filtered = list(
            filter(lambda x: any(f["name"] == x["name"] for f in self.subdomains), records)
        )
        return filtered
    
    def update_subdomain_record(self, new_value: str, record_id: str, subdomain: str) -> Any:
        proxied = self.__find_proxy_config_for_subdomain__(subdomain=subdomain)
        self.logger.info(f"Attempting to update records for {subdomain} with value {new_value} and proxy: '{proxied}'")
        return self.client.zones.dns_records.put(self.zone_id, record_id, data = {
            "name": subdomain,
            "type": "A",
            "content": new_value,
            "proxied": proxied
        })
    
    def __find_proxy_config_for_subdomain__(self, subdomain: str) -> bool:
        proxy = True
        matching_config = [
            saved_subdomain for saved_subdomain in self.subdomains 
            if saved_subdomain["name"] == subdomain
        ]
        if len(matching_config) > 0:
            proxy_config = matching_config[0]["proxy"]
            self.logger.info(f"Found proxy configuration for subdomain {subdomain}: {proxy_config}")
            proxy = proxy_config
        else:
            self.logger.info(f"The proxy configuration for subdomain {subdomain} is missing. Using default: true")

        return proxy

