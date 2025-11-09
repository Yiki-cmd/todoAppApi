import csv
import json
import logging
from io import StringIO

from app.core.config import settings


# Custom logging formatters
class JSONFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_record = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
        }
        return json.dumps(log_record)


class CSVFormatter(logging.Formatter):
    def __init__(self, fmt: str | None = None, datefmt: str | None = None) -> None:
        super().__init__(fmt, datefmt)
        self.output = StringIO()
        self.writer = csv.writer(self.output)

    def format(self, record: logging.LogRecord) -> str:
        self.output.seek(0)
        self.output.truncate(0)
        self.writer.writerow(
            [
                self.formatTime(record, self.datefmt),
                record.levelname,
                record.getMessage(),
            ]
        )
        return self.output.getvalue().strip()

    def get_logger(name: str | None = None) -> logging.Logger:
    log_level = getattr(logging, settings.log_level.upper(), logging.DEBUG)
    logging.root.setLevel(log_level)

    # Choose a formatter based on the log_format setting
    default_log_format = "%(asctime)s - %(levelname)s - %(message)s"
    formatter: logging.Formatter
    if settings.log_format == "csv":
        formatter = CSVFormatter(datefmt=settings.log_date_format)

    elif settings.log_format == "json":
        formatter = JSONFormatter(datefmt=settings.log_date_format)

    elif settings.log_format == "yaml":
        formatter = yamlFormater(datefmt=settings.log_date_format)  # noqa: F821

    else:  # default to text formatting
        formatter = logging.Formatter(
            default_log_format, datefmt=settings.log_date_format
        )


logger = logging.getLogger("multi")
logger.setLevel(logging.DEBUG)

# cosnole Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)


# File handler
file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter("%(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("This goes to console only")
logger.error("This goes to console AND file")
