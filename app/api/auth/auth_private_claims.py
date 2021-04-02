from app.utils.response import JsonResponse
from app.utils.token import decode_jwt


async def get_auth_payload_data():
    try:
        payload = decode_jwt(token=token, check_expiration=False)
    except Exception:
        return JsonResponse(message='Cannot Decode Token', code=400, success=False)
