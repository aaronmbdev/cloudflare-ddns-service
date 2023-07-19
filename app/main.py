from setup import DDNSSetup
from start import DDNSStart
from utils.argparser import ArgsComposer
from utils.logging import LoggingManager

def main():
    LoggingManager()
    args_composer = ArgsComposer.get()
    args = args_composer.parse_args()
    valid_args = ArgsComposer.validate_args(args)
    if not valid_args:
        exit()

    if args.command == "setup":
        DDNSSetup().setup_ddns_service(args)

    if args.command == "start":
        DDNSStart()
    

if __name__ == "__main__":
    main()
