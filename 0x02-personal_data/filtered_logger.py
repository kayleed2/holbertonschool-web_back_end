#!/usr/bin/env python3
"""
function called filter_datum
that returns the log message
obfuscated
"""

import re
from typing import List


def filter_datum (fields: List[str], redaction: str, message: str, separator: str) -> str:
    """a function called filter_datum
    that returns the log message obfuscated:"""
    for el in fields:
        pattern = f"(?<={el}=).*?(?={separator})"
        string = re.sub(pattern, redaction, message)
    return message
