import sqlalchemy as sa
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api import routes
from app.config import settings
from app.utils.response import JsonResponse
from app.version import API_VERSION, API_NAME

app_kwargs = dict(
    docs_url=f'/api/{API_VERSION}/docs',
    redoc_url=f'/api/{API_VERSION}/redoc',
    openapi_url=f'/api/{API_VERSION}/openapi.json'
)

if not settings.ENABLE_API_DOCS:
    app_kwargs.update(dict(docs_url=None, redoc_url=None))

app = FastAPI(**app_kwargs, title=API_NAME, routes=routes)

# Config CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=getattr(settings, 'CORS_ALLOW_ORIGINS', '*').split(','),
    allow_methods=getattr(settings, 'CORS_ALLOW_METHODS', '*').split(','),
    allow_headers=getattr(settings, 'CORS_ALLOW_HEADERS', '*').split(','),
    allow_credentials=True,
)


# @app.on_event("startup")
# async def start_db():
#     db = settings.DB
#     app.db_engine = sa.create_engine(db, pool_recycle=settings.DB_POOL_RECYCLE)
#
#
# @app.middleware("http")
# async def connect_db(request: Request, call_next):
#     request.app.db = request.app.db_engine.connect()
#     response = await call_next(request)
#     request.app.db.close()
#     return response
#
#
# @app.on_event("shutdown")
# async def close_db(request: Request):
#     request.app.db.dispose()


@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    message: str = exc.detail
    code: int = exc.status_code
    status_code: int = code

    return JsonResponse(
        message=message,
        code=code,
        status_code=status_code
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    error_list = exc.errors()

    if len(error_list) == 1:
        # this "might" be a JSON error
        check_json_error = error_list[0]['loc'][1]
        if isinstance(check_json_error, int):  # int indicates json error character position
            return JsonResponse(
                message='Invalid JSON',
                code=400,
                success=False,
                status_code=400
            )

    error_messages = {}
    for error in error_list:
        error_messages.update(
            {error['loc'][1]: error['msg']}
        )

    return JsonResponse(
        data=error_messages,
        message='Please check your data',
        code=400,
        success=False,
        status_code=400
    )
