import datetime

from app.schema.user_auth import RegisterAccount
from app.utils.response import JsonResponse
from app.utils.string import convert_string_data_to_datetime
from app.utils.token import get_password
from app.utils.user import check_user_status, create_user


async def register(register: RegisterAccount):
    user = check_user_status(register.phone)

    now_time = datetime.datetime.now()

    password = get_password(4)

    if user is not None:
        return JsonResponse(message='User already existed')
    else:
        create_user(phone=register.phone, name=register.name, password=password, register_at=now_time)

    result = {
        'name': register.name,
        'phone': register.phone,
        'password': password,
        'register_at': convert_string_data_to_datetime(now_time),
    }

    return JsonResponse(data=result, message='Successfully Register')
