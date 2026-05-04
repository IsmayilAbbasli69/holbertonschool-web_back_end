#!/usr/bin/env python3
"""
Module that handles the database engine/session

Handles user data
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base
from user import User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Returns a User object and saves it to the database
        """
        my_user = User(email=email, hashed_password=hashed_password)
        self._session.add(my_user)
        self._session.commit()
        return my_user

    def find_user_by(self, **kwargs) -> User:
        """
        Returns a User object if found in database

        NoResultFound and InvalidRequestError are raised when no results
        are found, or when wrong query arguments are passed, respectively.
        """
        for key in kwargs.keys():
            if key not in User.__table__.columns:
                raise InvalidRequestError()
        result = self._session.query(User).filter_by(**kwargs).one_or_none()
        if not result:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        Uses find_user_by to locate user and then updates it

        If an arg doesn't correspond to the user, raise ValueError
        """
        user = self.find_user_by(id=user_id)

        for arg, value in kwargs.items():
            if not hasattr(user, arg):
                raise ValueError()
            setattr(user, arg, value)
        self._session.commit()
