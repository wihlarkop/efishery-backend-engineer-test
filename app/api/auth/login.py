from app.schema.user_auth import LoginAccount
from app.utils.response import JsonResponse
from app.utils.token import generate_access_token
from app.utils.user import check_user_status


async def login(login: LoginAccount):
    user = check_user_status(login.phone)
    print(user)

    if user is None:
        return JsonResponse(message='User does not exist', code=404)

    if user.get('password') != login.password:
        return JsonResponse(message='Invalid password')

    access_token = generate_access_token(phone=user.get('phone'),
                                         name=user.get('name'),
                                         password=user.get('password'),
                                         register_at=user.get('register_at'),
                                         role=user.get('role'))

    result = {
        'phone': user.get('phone'),
        'name': user.get('name'),
        'access_token': access_token
    }

    return JsonResponse(data=result)
