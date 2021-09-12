from fastapi_mail import FastMail, MessageSchema
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from app.config import settings
from app.utils import generate_link_token


async def send_confirm_email(form, background):
    name = form.get('name')
    email = form.get('email')

    token = generate_link_token(email)
    link = '{}/register/user/{}'.format(settings.URL, token)

    html = '''
        <p>Seja bem vindo {}<p>
        <a href={} target="_blank">Confirme seu email</a>
    '''.format(name, link)

    try:
        message = MessageSchema(
            subject='Email de Confirmação',
            recipients=[email],
            body=html,
            subtype='html'
        )
        fm = FastMail(settings.EMAIL_CONFIG)
        background.add_task(fm.send_message, message)
        return JSONResponse(status_code=HTTP_200_OK,
                            content={
                                'status': True,
                                'message': 'Convite enviado com sucesso!'
                            }
                            )
    except Exception:
        return JSONResponse(status_code=HTTP_200_OK,
                            content={
                                'status': False,
                                "message": "Problemas na confirmação do seu email, por favor, tente novamente."
                            })
