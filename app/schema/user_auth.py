from pydantic import BaseModel, constr


class RegisterAccount(BaseModel):
    name: str
    phone: int


class LoginAccount(BaseModel):
    phone: int
    password: constr(max_length=4)
