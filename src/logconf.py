import logging.config

from project.settings import settings

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "{levelname} APP:{name}; {asctime} {module} "
                "{process:d} {thread:d}  LINE:{lineno} {message}"
            ),
            "style": "{",
        },
        "simple": {
            "format": "{levelname} LINE:{lineno} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file_log": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": f"{settings.LOG_DIR}/logs/file.log"
        }
    },
    "loggers": {
        "base": {
            "handlers": ["file_log", "console"],
            "level": "INFO",
        },
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger("base")
