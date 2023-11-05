from sqlalchemy import Column, Integer, Text, VARCHAR

from .meta import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(255), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    role = Column(Text, nullable=False, default="user")
