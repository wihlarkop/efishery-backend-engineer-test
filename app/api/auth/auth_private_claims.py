from fastapi import Request
from app.utils.response import JsonResponse
from app.utils.token import get_payload


async def get_auth_payload_data(request: Request):
    authorization: str = request.headers.get('Authorization')

    print(authorization)

    token = authorization.replace('Bearer ', '')

    data = get_payload(token)

    return JsonResponse(data=data)
