
import argparse


class ArgsComposer:
    def get(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--cloudflare-key", type=str, required=True)

        return parser
