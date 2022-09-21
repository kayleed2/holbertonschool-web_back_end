#!/usr/bin/env python3
"""Module to create auth class"""


from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import re
from base64 import b64decode
from models.user import User


class SessionAuth(Auth):
    """class to define session authorization"""
