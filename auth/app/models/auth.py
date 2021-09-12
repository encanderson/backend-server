from pydantic import BaseModel, create_model


class Login(BaseModel):
    email: str
    password: str


class ResponseLogin(BaseModel):
    status: bool
    message: str
    user: create_model('User', name=(str, None), email=(str, None)) = None
    token: str = None


class SendCode(BaseModel):
    email: str


class ChangePassword(BaseModel):
    password: str
    email: str


class GenericResponse(BaseModel):
    status: bool
    message: str


class CodeResponse(BaseModel):
    status: bool
    message: str
    code: int
    email: str
