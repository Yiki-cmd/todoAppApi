import csv
import json
import logging
from io import StringIO

from dotenv import load_dotenv

load_dotenv()


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


LOG_FILE = os.getenv("LOG_FILe", "/var/log/app.log")


def get_logger() -> None:
    loggin.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format=JSONFormatter(),
        handlers=[logging.StreamHandler()],
    )
