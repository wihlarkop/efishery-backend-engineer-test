import datetime
import random
import string
import jwt

from app.config import settings


def generate_access_token(phone: int, name: str, password: str, register_at: str, role: str = 'user'):
    expiration = datetime.datetime.now() + datetime.timedelta(seconds=settings.AUTH_TOKEN_EXPIRATION)
    payload = {
        'phone': phone,
        'name': name,
        'password': password,
        'register_at': register_at,
        'role': role,
        'exp': int(expiration.timestamp())
    }

    access_token = encode_jwt(payload)

    return access_token


def get_password(size: int):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def decode_jwt(token: str, check_expiration: bool = True):
    payload = jwt.decode(token, algorithms='HS256', key=settings.SECRET_KEY, verify_expiration=check_expiration)
    return payload


def encode_jwt(payload: dict):
    token = jwt.encode(payload, key=settings.SECRET_KEY)
    return token


def get_payload(token: str, check_expiration: bool = True, raise_error: bool = True):
    try:
        payload = decode_jwt(token, check_expiration=check_expiration)
    except jwt.exceptions.PyJWTError as e:
        if raise_error:
            raise e

        return None
    return payload
