from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK
from app.database.mongo import db
from app.utils.authentication import Bcrypt
from app.utils import hashFunction
from app.utils.send_email import send_confirm_email


async def create_user(user, background):
    """
    function to create user

    Args:
        user (dict{
            name, email, password
        }): basic information to create user

    Returns:
        dict{
            status: bool,
            message
        }: True, if create with success, False if not.
    """
    password = user.get('password')
    email = user.get('email')

    user['_id'] = hashFunction(email)

    hash_password = Bcrypt.generate_hash_password(password)
    user['password'] = hash_password
    try:
        resp = db.insert('users', user)

        if resp.acknowledged:
            await send_confirm_email(user.get('name'), background)
            return {
                'status': True,
                'message': 'Usuário adicionado com sucesso!'
            }
        else:
            return {
                'status': False,
                'message': 'Houve um erro no regsitro, por favor, tente novamente.'
            }
    except Exception:
        return {
            'status': False,
            'message': 'Usuário já existe!'
        }
