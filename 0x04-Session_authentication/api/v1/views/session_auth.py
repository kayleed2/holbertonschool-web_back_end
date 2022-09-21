#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response, session
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles all routes for session authentication"""
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}, 400)
    if pwd is None:
        return jsonify({"error": "password missing"}, 400)

    users = User.search({'email': email})

    if users == []:
        return jsonify({"error": "no user found for this email"}, 404)

    for el in users:
        if not el.is_valid_password(pwd):
            return (jsonify({"error": "wrong password"}), 401)
        else:
            from api.v1.app import auth
            session_id = auth.create_session(el.id)
            sesh = getenv('SESSION_NAME')
            session_id[sesh] = session_id
            # response = jsonify(el.to_json())
            # response.set_cookie(getenv('SESSION_NAME'), session_id)
            return session_id
