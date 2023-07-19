import CloudFlare

class CloudflareService:
    def __init__(self, config: dict) -> None:
        self.client = CloudFlare.CloudFlare(
            token=config.cloudflare_token,
            email=config.email
        )