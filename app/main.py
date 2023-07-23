from app.setup import DDNSSetup
from app.start import DDNSStart
from app.utils.argparser import ArgsComposer
from app.utils.logging import LoggingManager

def main():
    LoggingManager()
    composer = ArgsComposer()
    parser = composer.get()
    args = parser.parse_args()
    valid_args = composer.validate_args(args)
    if not valid_args:
        exit()

    if args.command == "setup":
        DDNSSetup().setup_ddns_service(args)

    if args.command == "start":
        DDNSStart(args).launch()
    

if __name__ == "__main__":
    main()
