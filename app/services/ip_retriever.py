import logging
from typing import Any
import requests


class IPRetriever:
    def find(self) -> Any:
        logger = logging.getLogger("ddns")
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            if response.status_code == 200:
                data = response.json()
                ip_address = data.get("ip")
                logger.info(f"The current IP address for this device is {ip_address}")
                return ip_address
            else:
                logger.error(f"Failed to retrieve IP address. Status code: {response.status_code}")
        except requests.RequestException as e:
            logger.error(f"There as an error trying to reach the IP Finding Service: {e}")
        return None
