import logging

logging.getLogger("urllib3").setLevel(logging.CRITICAL)


class AnsiColoredFormatter(logging.Formatter):
    COLOR_MAP = {
        "DEBUG": "\033[36m",
        "INFO": "\033[32m",
        "WARNING": "\033[33m",
        "ERROR": "\033[31m",
        "CRITICAL": "\033[35m",
    }
    RESET = "\033[0m"

    def format(self, record):
        levelname_color = self.COLOR_MAP.get(record.levelname, self.RESET)
        record.levelname = f"{levelname_color}{record.levelname}{self.RESET}"
        return super().format(record)


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s]: %(message)s",
    handlers=[logging.StreamHandler()],
)

for handler in logging.root.handlers:
    handler.setFormatter(AnsiColoredFormatter("[%(levelname)s]: %(message)s"))

logger = logging.getLogger(__name__)
