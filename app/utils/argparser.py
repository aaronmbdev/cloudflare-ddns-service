
import argparse


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
        setup.add_argument("--cloudflare-key", type=str, required=False, help="Cloudflare API Key")
        setup.add_argument("--domain", type=str, required=False, help="Domain to keep updated")

        return parser
