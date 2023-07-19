import argparse
import logging

class ArgsComposer:
    def get() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "command", 
            type=str, 
            help="Comando to execute. Could be setup or start",
            choices=["setup", "start"]
        )
        setup = parser.add_argument_group("setup", "Setup DDNS Configuration")
        setup.add_argument("--cloudflare-token", type=str, required=False, help="Cloudflare API Token")
        setup.add_argument("--domain", type=str, required=False, help="Domain to keep updated")
        setup.add_argument("--email", type=str, required=False, help="Cloudflare email")

        return parser
    
    def validate_args(args: argparse.ArgumentParser) -> bool:
        logger = logging.getLogger("ddns")
        if args.command == "setup":
            if args.domain == None or args.cloudflare_token == None or args.email == None:
                logger.error("You must specify a Cloudflare API Key, Cloudflare Token, email and domain name to setup DDNS. Use ddns -h")
                return False
        return True
