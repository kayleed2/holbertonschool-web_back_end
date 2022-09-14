#!/usr/bin/env python3
"""
Encrypt password module
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """Takes password as string and hashes it"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks is password is valid or not"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
