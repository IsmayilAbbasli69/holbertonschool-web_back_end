#!/usr/bin/env python3
"""
Creates Flask app
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    First get endpoint
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """
    Expects two form data fields: "email" and "password".

    If the user does not exist, registers it and responds.

    If user already exists, catch exception and return JSON payload and
        returns 400
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({'email': email, 'message': 'user created'})
    except ValueError as e:
        return jsonify({'message': 'email already registered'}), 400


@app.route("/sessions", methods=["POST"])
def sessions():
    """
    Expects two form data fields: "email" and "password".

    If login info is incorrect, use flask.abort to respond with 401.

    Otherwise, create new session for the user, store the session_id as
    a cookie with key "session_id" and returns JSON payload of form.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password or not AUTH.valid_login(email, password):
        abort(401)
    sesh_id = AUTH.create_session(email)
    result = jsonify({'email': email, 'message': 'logged in'})
    result.set_cookie('session_id', sesh_id)
    return result


@app.route("/sessions", methods=["DELETE"])
def logout():
    """
    Expected to contain session_id as cookie.

    Finds user with requested session_id. If user exists, delete session
    and redirect the user to 'GET /'. If the user does not exist,
    respond with 403.
    """
    sesh_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sesh_id)
    if not user or not sesh_id:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/', 302)


@app.route("/profile", methods=["GET"])
def profile():
    """
    Expected to contain a session_id cookie.

    Uses session_id to find user. If the user exists, respond with 200
    and JSON payload of form. If the user does not exist or the
    session_id is invalid, respond with 403.
    """
    sesh_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(sesh_id)
    if not user or not sesh_id:
        abort(403)
    return jsonify({'email': user.email})


@app.route("/reset_password", methods=["POST"])
def reset_password():
    """
    Expected to contain email field.

    If email is not registered, responds with 403. Otherwise,
    generates a token and responds with 200 and JSON payload of form.
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({'email': email, 'reset_token': token})
    except Exception as e:
        abort(403)


@app.route("/reset_password", methods=["PUT"])
def reset_password_change():
    """
    Expected to contain email, reset_token, and new_password fields.

    Updates the password.

    If token is invalid, catches exception and responds with 403.

    Otherwise, responds with 200 and JSON payload of form.
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({'email': email, 'message': 'Password updated'})
    except Exception as e:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
