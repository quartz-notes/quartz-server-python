import uuid
from sqlalchemy import UUID, Boolean, Column, ForeignKey, String
from app.core.db import Base
from sqlalchemy.types import Uuid


class UserDB(Base):
    __tablename__ = "users"
    id = Column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)


class NoteDB(Base):
    __tablename__ = "notes"
    id = Column(
        Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    title = Column(String, index=True)
    content = Column(String)
    owner_id = Column(UUID, ForeignKey("users.id"))
