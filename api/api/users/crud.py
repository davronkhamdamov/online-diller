import datetime
import uuid
from typing import Optional

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from api.api.models import Users
from api.api.schemas import UserSchema


def get_user(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    order_by: Optional[str] = None,
    search: Optional[str] = None,
    debt: Optional[str] = None,
):
    if skip < 0:
        skip = 0
    query = db.query(Users)
    if search:
        search = f"%{search}%"
        query = query.filter(or_(Users.name.ilike(search), Users.surname.ilike(search)))
    if debt == "true":
        query = query.filter(Users.balance < 0)

    if order_by == "descend":
        query = query.order_by(Users.name.desc())
    elif order_by == "ascend":
        query = query.order_by(Users.name.asc())
    else:
        query = query.order_by(Users.created_at.desc())

    return query.offset(skip * limit).limit(limit).all()


def count_users(db: Session):
    return db.query(func.count(Users.id)).scalar()


def get_users(db: Session):
    return db.query(Users).all()

def get_user_by_id(db: Session, user_id: uuid.UUID):
    return db.query(Users).filter(Users.id == user_id).first()


def create_user(db: Session, user: UserSchema):
    _user = Users(
        name=user.name,
        surname=user.surname,
        job=user.job,
        gender=user.gender,
        date_birth=user.date_birth,
        address=user.address,
        description=user.description,
        created_at=datetime.datetime.now().isoformat(),
        phone_number=user.phone_number,
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def delete_user(db: Session, user_id: uuid.UUID):
    db.query(Users).filter(Users.id == user_id).delete()
    db.commit()


def update_user(db: Session, user: UserSchema, user_id: uuid.UUID):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.name = user.name
    _user.surname = user.surname
    _user.job = user.job
    _user.date_birth = user.date_birth
    _user.address = user.address
    _user.description = user.description
    _user.gender = user.gender
    _user.updated_at = datetime.datetime.now().isoformat()
    _user.phone_number = user.phone_number
    _user.updated_at = datetime.datetime.now()
    db.commit()
    db.refresh(_user)
    return _user


def update_user_image(db: Session, img_url: str, user_id: uuid.UUID):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.img_url = img_url
    _user.updated_at = datetime.datetime.now()
    db.commit()
    db.refresh(_user)
    return _user
