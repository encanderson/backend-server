from fastapi import APIRouter, BackgroundTasks, Depends
from app.models.register import Register, ResponseRegister
from app.utils.register import create_user
from app.utils.authentication import Authentication
from app.utils import verify_token

register = APIRouter()


@register.post('/user', tags=['Registro'], response_model=ResponseRegister)
async def register_user(register: Register, background: BackgroundTasks):
    user = register.dict()
    resp = await create_user(user, background)
    return resp


@register.get('/user/{user}', tags=['Registro'], response_model=ResponseRegister)
async def confirm_user(user: str):
    resp = verify_token(user)
    if resp.get('status'):
        auth = Authentication()
        await auth.confirm_user(resp.get('message'))
    return resp
