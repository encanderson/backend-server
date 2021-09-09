from fastapi import APIRouter
from app.models.auth import ResponseLogin, Login
from app.utils.authentication import Authentication

login = APIRouter()


@login.post('/login', tags=['Autenticação'], response_model=ResponseLogin)
async def sign_in(login: Login):
    form = login.dict()
    auth = Authentication()
    resp = await auth.verify_user(form)
    return resp
