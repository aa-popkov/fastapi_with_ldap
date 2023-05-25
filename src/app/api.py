from fastapi import Body, Depends, FastAPI
from pydantic import BaseModel
from auth.bearer import JWTBearer
from auth.models import UserLoginSchema
from auth.ldap import AuthLDAP
from auth.token_auth import signJWT
from datetime import datetime

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    exp: int | None


def check_user(data: UserLoginSchema):
    ldap_auth_result: dict = AuthLDAP().auth(data.username, data.password)
    if ldap_auth_result.get("state"):
        return True
    return False


@app.post('/')
async def index(user: User) -> dict:
    return {
        "status": "succes",
        "msg": {
            "text": f"Hello {user.name}!"
        },
        "user": user
    }

@app.post("/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.username)
    return {
        "error": "Wrong login details!"
    }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(post: str) -> dict:
    return {
        "data": "post added."
    }

