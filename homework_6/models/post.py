__all__ = ("Post",)

from .user import User
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from .database import db


class Post(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    pre_post = Column(String(30))
    post_text = Column(Text, nullable=False)
    user_username = Column(String, ForeignKey("user.username"))   # Отношение один-ко-много пользоватлей к постам по имени пользователя
    user = relationship("User", backref="posts")

    def __str__(self):
        return (f"Username: {self.user_username}\n"
                f"{__class__.__name__}: {self.post_text}\n"
                "------------")

    def __repr__(self):
        return str(self)
