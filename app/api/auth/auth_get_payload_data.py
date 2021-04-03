from fastapi import Request
from app.utils.response import JsonResponse
from app.utils.token import get_payload


async def auth_get_payload_data(request: Request):
    authorization: str = request.headers.get('Authorization')

    token = authorization.replace('Bearer ', '')

    data = get_payload(token)

    return JsonResponse(data=data)
