from passlib.context import CryptContext
from app.database.mongo import db
from app.utils import generate_token


class Bcrypt:
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @staticmethod
    def generate_hash_password(password):
        return Bcrypt.pwd_context.hash(password)

    @staticmethod
    def verify_password(password, hashed_password):
        return Bcrypt.pwd_context.verify(password, hashed_password)


class Authentication(Bcrypt):
    def __init__(self):
        pass

    async def verify_user(self, form):
        email = form.get('email')
        password = form.get('password')

        user = db.find_one('users', {
            'email': email
        }, {
            '_id': 0,
            'email': 1,
            'name': 1,
            'password': 1
        })
        if user:
            if not self.verify_password(password, user.get('password')):
                return {
                    'status': False,
                    'message': 'Senha não está correta.'
                }
            else:
                user.pop('password')
                token = await generate_token(email)
                return {
                    'status': True,
                    'message': 'Login realizado com sucesso!',
                    'user': user,
                    'token': token
                }
        else:
            return {
                'status': False,
                'message': 'Usuário não existe, confire se dos dados estão corretos.'
            }

    @staticmethod
    async def confirm_user(email):
        db.update('users', {
            'email': email
        }, {
            '$set': {
                'confirmEmail': True
            }
        })
    
    async def change_password(self, form):
        password = form.get('password')
        email = form.get('email')
        hash_password = self.generate_hash_password(password)
        db.update('users', {
            'email': email
        }, {
            '$set': {
                'password': hash_password
            }
        })
