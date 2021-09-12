from fastapi import APIRouter
from app.register.routes import register
from app.login.routes import login
from app.auth.routes import auth

router = APIRouter()

router.include_router(register, prefix='/register')
router.include_router(login, prefix='/authentication')
router.include_router(auth, prefix='/auth')
