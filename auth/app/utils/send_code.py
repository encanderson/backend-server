from fastapi_mail import FastMail, MessageSchema
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from app.config import settings
from app.utils import access_cod
from app.database.mongo import db


async def send_email_code(form, background):
    code = access_cod(6)
    email = form.get('email')

    user = db.find_one('users', {
        'email': email
    }, {
        '_id': 0,
        'name': 1
    })

    if user:
        name = user.get('name')

        html = '''
            <p>{}, confirme seu códido de acesso<p>
            <p> Códgo: {}<p>
        '''.format(name, code)

        try:
            message = MessageSchema(
                subject='Código de Confirmação',
                recipients=[email],
                body=html,
                subtype='html'
            )
            fm = FastMail(settings.EMAIL_CONFIG)
            background.add_task(fm.send_message, message)
            return JSONResponse(status_code=HTTP_200_OK,
                                content={
                                    'status': True,
                                    'message': 'Códgo enviado com sucesso!',
                                    'code': code,
                                    'email': email
                                }
                                )
        except Exception:
            return JSONResponse(status_code=HTTP_200_OK,
                                content={
                                    'status': False,
                                    "message": "Problemas no envio do código, por favor, tente novamente.",
                                    'code': None,
                                    'email': None
                                })
    else:
        return JSONResponse(status_code=HTTP_200_OK,
                            content={
                                'status': False,
                                "message": "Email do usuário não existe, por favor confire seus dados.",
                                'code': None,
                                'email': None
                            })
