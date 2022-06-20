__all__ = ("User",)

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)
from .database import db


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(255), unique=True, nullable=False)
    logged_in = Column(Boolean, default=False, nullable=True)
    logged_out = Column(Boolean, default=False, nullable=True)

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id}, "
            f"username={self.username!r}, "
            f"password={self.password}, "
            f"logged_in={self.logged_in})"
        )

    def __repr__(self):
        return str(self)
