#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re


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
            new = re.split("\s", authorization_header, 1)
            if len(new) != 2:
                return None
            return new[1]
