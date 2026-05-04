#!/usr/bin/env python3
"""This file we use for create auth funct in our app"""
from flask import request
from typing import List, TypeVar


class Auth:
    """We gonna use that class for auth goals"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """This funct is require the auth"""
        if path is None or (excluded_paths is None or []):
            return True
        normalized_path = path if path.endswith('/') else path + '/'
        if normalized_path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """This funct is auto header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """This funct is checking current user"""
        return None
