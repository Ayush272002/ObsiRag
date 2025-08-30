from .config import Base
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, Text

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    embedding = Column(Vector(384))
    source = Column(Text, nullable=False)