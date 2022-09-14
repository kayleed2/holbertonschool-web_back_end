#!/usr/bin/env python3
"""
function called filter_datum
that returns the log message
obfuscated
"""

import re
from typing import List
import logging
from os import environ
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Function to return a logging obj"""
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    user_data.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    user_data.addHandler(handler)
    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """function that returns a connector to the database"""
    db = mysql.connector.connect(
        host=environ.get("PERSONAL_DATA_DB_HOST"),
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),
        database=environ.get("PERSONAL_DATA_DB_NAME")
    )
    return db


def main():
    """obtain a database connection using
    get_db and retrieve all rows in the users table"""
    log = get_logger()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        informationList = row.items()
        item = "; ".join(f"{tuple[0]}={tuple[1]}" for el in informationList)
        log.info(item)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
