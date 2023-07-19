import argparse
import logging

from utils.logging import LoggingManager

logger = logging.getLogger(__name__)

def main():
    LoggingManager().configure(1)
    

if __name__ == "__main__":
    main()
