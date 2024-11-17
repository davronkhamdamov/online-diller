import hashlib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.api.auth.router import router as auth_route
from api.api.models import Staffs
from api.api.users.router import router as user_router
from api.db import db1

admin = db1.query(Staffs).filter(Staffs.login == "admin").first()

if not admin:
    _staff = Staffs(
        name="admin",
        surname="admin",
        address="Uzb",
        login="admin",
        password=hashlib.sha256("admin".encode()).hexdigest(),
        phone_number="+99898765432",
        gender="male",
        role="admin",
    )
    db1.add(_staff)
    db1.commit()

db1.close()

app = FastAPI(docs_url="api/py/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_route, prefix="api/py/auth", tags=["Login"])
app.include_router(router=user_router, prefix="api/py/user", tags=["Users"])
