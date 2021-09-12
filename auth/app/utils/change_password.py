from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from app.utils.authentication import Authentication


async def change_password(form):
    auth = Authentication()
    try:
        await auth.change_password(form)
        return JSONResponse(status_code=HTTP_200_OK,
                            content={
                                'status': True,
                                "message": "Senha alterada com sucesso!",
                            })
    except Exception:
        return JSONResponse(status_code=HTTP_200_OK,
                            content={
                                'status': False,
                                "message": "Houve uma falha, se o problema persistir, entre em contato",
                            })
