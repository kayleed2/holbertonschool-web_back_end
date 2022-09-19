#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar


class Auth():
    """class to define authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns boolean of if user is auth"""
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == "":
            return True

        if path in excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """This will get flask request object"""
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """This will get flask request object"""
        return request
