#!/usr/bin/env python3
"""
Handles endpoints for session authentication
"""
from flask import jsonify, abort, request, session, make_response
from models.user import User
from api.v1.views import app_views
from os import getenv


SESSION_NAME = getenv("SESSION_NAME")


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def sess_auth() -> str:
    """
    POST /api/v1/auth_session/login

    Returns:
        - the status of the API
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None:
        return jsonify({"error": "email missing"}), 400
    if password is None:
        return jsonify({"error": "password missing"}), 400
    my_user = User.search({'email': email})
    if len(my_user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for u in my_user:
        if not u.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(my_user[0].id)
        user_id = auth.user_id_for_session_id(session_id)
        user = User.get(user_id)
        out = jsonify(user.to_json())
        out.set_cookie(SESSION_NAME, session_id)
        return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def delete_session() -> str:
    """
    DELETE /api/v1/auth_session/logout

    Returns:
        - the status of the API
    """
    from api.v1.app import auth
    session_id = request.cookies.get(SESSION_NAME)
    if session_id is None:
        abort(404)
    auth.destroy_session(request)
    return jsonify({}), 200
