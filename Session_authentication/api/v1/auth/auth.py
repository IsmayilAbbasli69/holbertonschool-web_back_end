#!/usr/bin/env python3
"""
Manage API authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


SESSION_NAME = getenv("SESSION_NAME")


class Auth():
    """
    Manage Api Authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """"
        Method that returns True if the <path> is not in the list of strings
        <excluded_paths>.

        You can assume <excluded_paths> contains string path always ending
        with a '/'.

        This method is slash intolerant. For example, if <path> is '/v1/auth'
        and <excluded_paths> is ['/v1/auth/', '/v1/auths/'], then this method
        will return False.

        Args:
            path(str): The path to check against <excluded_paths>
            excluded_paths(List[str]): The list of paths to check against

        Additional Returns:
            True if <path> is None
            True if <path> is None
            True if <excluded_paths> is None or empty
            False if <path> is in <excluded_paths>
        """
        if excluded_paths is None or not len(excluded_paths) or path is None:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        HTTP header authorization

        Args:
            request(Flask.request): The request object
            asdasd

        Returns:
            If <request> is None, returns None.
            If <request> doesn't contain the header key <'Authorization'>,
            returns None.
            Otherwise, returns the value of the header key <'Authorization'>.
        """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Args:
            request(Flask.request): The request object

        Returns:
            None

        """
        return None

    def session_cookie(self, request=None):
        """
        Returns a cookie value from a request

        Uses .get_cookies() to get the cookies from <request>

        Uses env variable <SESSION_NAME> to define the name of the cookie
            used for the session ID

        Args:
            request (obj): The request object

        Returns:
           None if <request> is None
           The value of the cookie named <_my_session_id> from <request> -
                the name of the cookie must be defined by the env variable
                    <SESSION_NAME>
        """
        if request is None:
            return None
        my_cookie = request.cookies.get(SESSION_NAME)
        return my_cookie
