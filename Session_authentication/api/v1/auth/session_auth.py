#!/usr/bin/env python3
"""
Session Authentication Module
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid
from os import getenv


class SessionAuth(Auth):
    """
    Handles Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a session ID for a <user_id>

        Args:
            user_id (str): The user's ID

        Returns:
            None if <user_id> is None
            None if <user_id> is not a string
            Otherwise:
                Generates a session ID using the `uuid` module and
                    uuid4() like <id> in <Base>
                Uses new session ID as key of the dict <user_id_by_session_id>,
                    the value for this key must be <user_id>
                Returns the session ID

        The same <user_id> can have multiple session IDs. The <user_id> is
            the value in the dictionary <user_id_by_session_id>
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        # assigns session_id to key, user_id to value
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns the user ID for a <session_id>

        Uses .get() to get the value for the key <session_id> in
        <user_id_by_session_id>

        Args:
            session_id (str): The session ID

        Returns:
            None if <session_id> is None
            None if <session_id> is not a string
            The value (The user ID) for the key <session_id> in
                <user_id_by_session_id>
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        my_session_id = self.user_id_by_session_id.get(session_id)
        return my_session_id

    def current_user(self, request=None):
        """
        Returns the <User> instance based on a cookie value

        Uses self.session_cookie(...) and self.user_id_for_session_id(...)
            to return the User ID based on the cookie <_my_session_id>

        By using this new User ID, you will be able to retrieve a <User>
            instance from the database. (You can use User.get())

        Args:
            request: request object

        Returns:
            User instance based on a cookie value
        """
        _my_session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(_my_session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout

        Args:
            request: request object

        Returns:
            If request is None, return False
            if request doesn't contain the session ID, return False
            if the session ID is not linked to any user ID, return False
            Otherwise, delete in <self.user_id_by_session_id> the key
                <session_id> and return True
        """
        if request is None:
            return False
        _my_session_id = self.session_cookie(request)
        if _my_session_id is None:
            return False
        user_id = self.user_id_for_session_id(_my_session_id)
        if user_id is None:
            return False
        del self.user_id_by_session_id[_my_session_id]
        return True
