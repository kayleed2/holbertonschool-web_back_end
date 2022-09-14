#!/usr/bin/env python3
"""
function called filter_datum
that returns the log message
obfuscated
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initiate class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """Formatting the record"""
        ms = super().format(record)
        return filter_datum(self.fields, self.REDACTION, ms, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function called filter_datum
    that returns the log message obfuscated:"""
    for el in fields:
        pattern = f"(?<={el}=).*?(?={separator})"
        message = re.sub(pattern, redaction, message)
    return message
