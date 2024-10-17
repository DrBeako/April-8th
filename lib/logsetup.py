from logging.config import dictConfig
import os


def init_log():

    # Generate required directory and file for logging config.
    os.makedirs('./logs', exist_ok=True)
    if not os.path.exists('./logs/.log'):
        open('./logs/.log', 'w').close()

    config: dict[
        str, int | bool | dict[str, dict[str, str]] | dict[str, dict[str, str] | dict[str, str | int]] | dict[
            str, dict[str, list[str] | str | bool]]] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(asctime)s [%(msecs)8d] %(levelname)-8s: %(module)-16s@%(funcName)-16s #%(lineno)-4d : %(message)s",
                "datefmt": "%Y-%m-%dT%H:%M:%S"
            },
            "async": {
                "format": "%(asctime)s [%(msecs)8d] %(levelname)s %(module)-16s@%(funcName)-16s #%(lineno)-4d %(processName)s[%(process)d] %(threadName)s[%(thread)d]: %(message)s"
            },
            "console": {
                "format": "%(asctime)s %(levelname)s %(module)-8s: %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "WARNING",
                "class": "logging.StreamHandler",
                "formatter": "console"
            },
            "file": {
                "level": "DEBUG",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "formatter": "verbose",
                "when": "midnight",
                "filename": "logs/.log",
                "interval": 1,
                "backupCount": 7
            }
        },
        "loggers": {
            "discord": {
                "handlers": ["file", "console"],
                "level": "INFO",
                "propagate": False,
            },
            "bot": {
                "handlers": ["file", "console"],
                "level": "INFO",
                "propagate": False,
            }
        }
    }
    dictConfig(config)
