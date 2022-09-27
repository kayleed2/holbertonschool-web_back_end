#!/usr/bin/env python3
"""
File that contains a hasing of a password method
"""
from base64 import encode
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hashes a password given as argument"""
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)
