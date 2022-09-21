#!/usr/bin/env python3
"""Module to create auth class"""


from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """class to define session authorization"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates session"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id