#!/usr/bin/env python3
"""
Encrypt password module
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Takes password as string and hashes it"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
