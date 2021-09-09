from hashlib import sha256
import datetime
from app.config import settings
import jwt


def hashFunction(data):
    hashed = sha256(data.encode("UTF-8")).hexdigest()
    return hashed


async def generate_token(_id):
    token = jwt.encode({
        '_id': _id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)
    }, settings.SECRET_KEY)

    return token.decode('utf-8')


def generate_link_token(_id):
    token = jwt.encode({
        '_id': _id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=7200)
    }, settings.SECRET_KEY)

    return token.decode('utf-8')


def verify_token(token):
    try:
        current_user = jwt.decode(
            token, settings.SECRET_KEY)
        return {
            'status': True,
            'message': current_user.get('_id')
        }
    except Exception:
        return {
            'status': False,
            'message': 'Token Inválido!'
        }
