import uuid
from datetime import datetime
from typing import Generic, TypeVar, Optional

from pydantic import BaseModel

T = TypeVar("T")


class UserSchema(BaseModel):
    id: Optional[uuid.UUID] = None
    name: str = None
    surname: str = None
    date_birth: datetime = None
    address: str = None
    phone_number: str = None
    gender: str = None
    job: str = None
    prikus: Optional[str] = None
    disease_progression: Optional[str] = None
    objective_check: Optional[str] = None
    milk: Optional[str] = None
    placental_diseases: Optional[str] = None
    description: Optional[str] = None
    balance: Optional[str] = None
    created_at: datetime = None
    updated_at: Optional[datetime] = None


class StaffsSchema(BaseModel):
    id: uuid.UUID = None
    name: str = None
    surname: str = None
    address: str = None
    login: Optional[str] = None
    password: Optional[str] = None
    phone_number: str = None
    gender: str = None
    color: str = None
    role: str = None
    foiz: int = None
    created_at: datetime = None
    updated_at: Optional[datetime] = None


class Response(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    total: Optional[int] = None
    result: Optional[T] = None
    info: Optional[dict] = None
    role: Optional[str] = None
    current_staff: Optional[dict] = None


class LoginSchema(BaseModel):
    login: str
    password: str
