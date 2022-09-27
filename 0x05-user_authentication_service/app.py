#!/usr/bin/env python3


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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
