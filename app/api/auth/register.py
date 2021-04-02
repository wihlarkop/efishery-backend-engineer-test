from app.schema.user_auth import RegisterAccount
from app.utils.response import JsonResponse
from app.utils.token import get_password
from app.utils.user import check_user_status, create_user


async def register(register: RegisterAccount):
    user = check_user_status(register.phone)

    password = get_password(4)

    if user is not None:
        return JsonResponse(message='User already existed')
    else:
        create_user(phone=register.phone, name=register.name, password=password)

    result = {
        'name': register.name,
        'phone': register.phone,
        'password': password
    }

    return JsonResponse(data=result, message='Successfully Register')
