#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """class to define authorization"""
    def extract_base64_authorization_header(self, authorization_header: str):
        """Returns the Base64 part of the Authorization
        header for a Basic Authentication"""
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        string = re.findall("Basic", authorization_header)
        if string == []:
            return None
        else:
            new = re.split(" ", authorization_header, 1)
            if len(new) != 2:
                return None
            return new[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str):
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            return b64decode(base64_authorization_header).decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None

        if type(decoded_base64_authorization_header) is not str:
            return None, None

        if ':' in decoded_base64_authorization_header:
            return decoded_base64_authorization_header.split(':')
        else:
            return None, None

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            search = User.search({'email': user_email})

            for user in search:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception:
            return None
