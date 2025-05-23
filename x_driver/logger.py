import logging

from colorlog import ColoredFormatter

logger = logging.getLogger("xdriver")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = ColoredFormatter(
    "%(log_color)s[-] XDRIVER %(levelname)-8s: %(message_log_color)s%(message)s",
    log_colors={
        "DEBUG": "white",
        "INFO": "cyan",
        "WARNING": "bold_yellow",
        "ERROR": "light_red",
        "CRITICAL": "bold_white,bg_red",
    },
    secondary_log_colors={
        "message": {
            "DEBUG": "white",
            "INFO": "cyan",
            "WARNING": "bold_yellow",
            "ERROR": "light_red",
            "CRITICAL": "bold_white,bg_red",
        }
    },
    style="%",
)
handler.setFormatter(formatter)
logger.addHandler(handler)
