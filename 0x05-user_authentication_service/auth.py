#!/usr/bin/env python3
"""
File that contains a hasing of a password method
"""

from db import DB
from base64 import encode
from bcrypt import hashpw, gensalt, checkpw
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers user and returns user object"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks if login is valid"""
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Method to get session id"""
        try:
            user = self._db.find_user_by(email=email)
            new_id = _generate_uuid()
            user.session_id = new_id
            return user.session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """Gets user from session id"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user


def _hash_password(password: str) -> bytes:
    """Hashes a password given as argument"""
    salt = gensalt()
    return hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """Genertaes a new uuid"""
    return str(uuid.uuid4())