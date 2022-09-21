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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Creates an instance method"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Overload that returns a User based on cookie"""
        _my_session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(_my_session_id)
        return User.get(user_id)
