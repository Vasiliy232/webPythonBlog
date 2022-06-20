__all__ = ("Tag",)

from .post import Post
from .associationtables import association_table
from sqlalchemy import (
    Column,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from .database import db


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    tag_text = Column(String(30))
    post = relationship("Post", secondary=association_table)

    def __str__(self):
        return f"{self.tag_text}"

    def __repr__(self):
        return str(self)
