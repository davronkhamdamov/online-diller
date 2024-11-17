import hashlib

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth.router import router as auth_route
from app.api.models import Staffs
from app.api.users.router import router as user_router
from app.db import db1

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

app = FastAPI(docs_url=None, redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_route, prefix="/auth", tags=["Login"])
app.include_router(router=user_router, prefix="/user", tags=["Users"])


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True)
