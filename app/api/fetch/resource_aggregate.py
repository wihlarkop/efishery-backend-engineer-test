from typing import Optional

from fastapi import HTTPException, Request, Query

from app.utils.user import check_user_status


async def get_resource_aggregate(request: Request, area: Optional[str] = Query(None),
                                 date: Optional[str] = Query(None)):
    user = check_user_status(request.state.payload.get('phone'))

    if user.get('role') != 'admin':
        raise HTTPException(status_code=403, detail="You don't have access")
