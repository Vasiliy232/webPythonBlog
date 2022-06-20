__all__ = ('association_table',)

from models import db
from sqlalchemy import (
    Column,
    ForeignKey,
)

association_table = db.Table(
    "association",
    db.Model.metadata,
    Column("post_id", ForeignKey("post.id")),
    Column("tag_id", ForeignKey("tag.id")),
)