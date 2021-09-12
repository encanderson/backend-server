from fastapi import APIRouter, BackgroundTasks
from app.utils.send_code import send_email_code
from app.models import auth as model_auth
from app.utils.change_password import change_password as change_pass


auth = APIRouter()


@auth.post('/recovery-password', tags=['Autenticação'],
           response_model=model_auth.CodeResponse)
async def send_code(email: model_auth.SendCode, background: BackgroundTasks):
    email = email.dict()
    resp = await send_email_code(email, background)
    return resp


@auth.put('/recovery-password', tags=['Autenticação'],
          response_model=model_auth.GenericResponse)
async def change_password(data: model_auth.ChangePassword):
    form = data.dict()
    resp = await change_pass(form)
    return resp
