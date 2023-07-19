import logging.config
import logging.handlers
import sys

BASE_LOGGING_CONFIGURATION = {
    "version": 1.0,
    "formatters": {
        "simple": {
            "format": "%(levelname)1.1s: %(asctime)s - %(message)s",
            "datefmt": None,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 1,
            "stream": sys.stdout,
        },
        "debug": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 10,
            "stream": sys.stdout,
        },
        "info": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 20,
            "stream": sys.stdout,
        },
        "warning": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 30,
            "stream": sys.stdout,
        },
        "error": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 40,
            "stream": sys.stdout,
        },
    },
    "root": {
        "level": 0,
        "handlers": {"console", "debug", "info", "warning", "error"},
    },
    "incremental": False,
    "disable_existing_loggers": False,
}

class LoggingManager:
    def configure(self, level: int):
        config = BASE_LOGGING_CONFIGURATION
        config["formatters"]["formatter"] = {
            "datefmt": None,
        }
        config["handlers"]["console"]["formatter"] = "formatter"
        config["handlers"]["console"]["level"] = level

        logging.config.dictConfig(config)

        logger = logging.getLogger()
        logger.setLevel(level)
        logger.propagate = False
        logger.info("Logging system configured successfully")

