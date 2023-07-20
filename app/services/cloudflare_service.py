import logging
from typing import Any
import CloudFlare


class CloudflareService:
    def __init__(self, config: dict) -> None:
        self.logger = logging.getLogger("ddns")
        self.domain = config["domain"]
        self.subdomain = config["subdomain"]
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
        

    def get_subdomain_records(self) -> Any:
        full_name = f"{self.subdomain}.{self.domain}"
        self.logger.info(f"Checking current DNS values for {full_name}")
        dns_records = self.client.zones.dns_records.get(self.zone_id)
        
        matching_record = [
            record for record in dns_records
            if record["name"] == full_name and record["type"] == "A"
        ]

        if len(matching_record) > 0:
            return {
                "id" : matching_record[0]["id"],
                "domain": matching_record[0]["name"],
                "value": matching_record[0]["content"]
            }
        return None
    
    def update_subdomain_record(self, new_value: str, record_id: str) -> Any:
        full_name = f"{self.subdomain}.{self.domain}"
        return self.client.zones.dns_records.put(self.zone_id, record_id, data = {
            "name": full_name,
            "type": "A",
            "content": new_value,
            "proxied": True
        })
