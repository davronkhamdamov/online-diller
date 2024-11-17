import datetime
import uuid

from sqlalchemy import Column, UUID, String, DateTime, Integer

from api.db import Base, engine


class Users(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    date_birth = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)
    img_url = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    job = Column(String, nullable=False)
    description = Column(String, nullable=True)
    balance = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


class Staffs(Base):
    __tablename__ = "staffs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True, nullable=False)
    surname = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    login = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    role = Column(String, default="user")
    img_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime)


Base.metadata.create_all(bind=engine)
