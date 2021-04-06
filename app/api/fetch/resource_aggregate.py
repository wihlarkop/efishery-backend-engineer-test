from itertools import groupby
from collections import defaultdict
from fastapi import HTTPException, Request

from app.utils.response import JsonResponse
from app.utils.scrape_resource import get_area_provinsi, scrape_resource
from app.utils.user import check_user_status


async def get_resource_aggregate(request: Request):
    user = check_user_status(request.state.payload.get('phone'))

    if user.get('role') != 'admin':
        raise HTTPException(status_code=403, detail="You don't have access")

    result = scrape_resource()

    INFO = sorted(result, key=get_area_provinsi)

    data = defaultdict(lambda: [])

    for key, value in groupby(INFO, get_area_provinsi):
        if key != '':
            data[key] = list(value)

    return JsonResponse(data=data)
