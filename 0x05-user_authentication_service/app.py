#!/usr/bin/env python3
"""Flask app is documented"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def message():
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'])
def users():
    email = request.form.get('email')
    pwd = request.form.get('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError:
        return jsonify({'message': 'email already registered'}), 400


@app.route('/sessions', methods=['POST'])
def login():
    email = request.form.get('email')
    pwd = request.form.get('password')

    if not email or not pwd:
        abort(401)
    if not (AUTH.valid_login(email=email, password=pwd)):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Logs user out"""
    inst = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(inst)
    if user is None or inst is None:
        abort(403)
    AUTH.destroy_session(inst)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """Implements a profile function"""
    inst = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(inst)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Implements a profile function"""
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token})
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """Implements the update password function"""
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        token = AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
