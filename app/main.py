import argparse
import logging
from utils.argparser import ArgsComposer
from utils.logging import LoggingManager

logger = logging.getLogger(__name__)

def main():
    LoggingManager().configure(1)
    args_composer = ArgsComposer.get()
    args = args_composer.parse_args()
    

if __name__ == "__main__":
    main()
