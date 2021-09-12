from pydantic import BaseModel, create_model


class Register(BaseModel):
    consents: create_model('Consents', privacy=(bool, ...), terms=(bool, ...))
    name: str
    email: str
    password: str


class ResponseRegister(BaseModel):
    status: bool
    message: str
