from fastapi import Depends
from fastapi.responses import PlainTextResponse
from fastapi.routing import APIRoute

from app.api.auth.login import login
from app.api.auth.register import register
from app.api.auth.auth_get_payload_data import auth_get_payload_data
from app.api.fetch.fetch_get_payload_data import fetch_get_payload_data
from app.api.fetch.resource_aggregate import get_resource_aggregate
from app.api.fetch.resource_list import get_resource_list
from app.version import API_VERSION
from app.utils.dependency import JWTBearer

prefix = f'/api/{API_VERSION}'


def alive():
    return 'alive'


routes = [
    APIRoute(f'{prefix}/alive', endpoint=alive, tags=['Status'], response_class=PlainTextResponse,
             response_description='Check Endpoint Status'),

    APIRoute(f'{prefix}/auth/register', endpoint=register, methods=['POST'], tags=['Auth'],
             response_class=PlainTextResponse),
    APIRoute(f'{prefix}/auth/login', endpoint=login, methods=['POST'], tags=['Auth'], response_class=PlainTextResponse),
    APIRoute(f'{prefix}/auth/payload', endpoint=auth_get_payload_data, tags=['Auth'], response_class=PlainTextResponse,
             dependencies=[Depends(JWTBearer())]),

    APIRoute(f'{prefix}/fetch/list-price', endpoint=get_resource_list, tags=['Fetch'],
             response_class=PlainTextResponse, dependencies=[Depends(JWTBearer())]),
    APIRoute(f'{prefix}/fetch/list-aggregate', endpoint=get_resource_aggregate, tags=['Fetch'],
             response_class=PlainTextResponse, dependencies=[Depends(JWTBearer())]),
    APIRoute(f'{prefix}/fetch/payload', endpoint=fetch_get_payload_data, tags=['Fetch'],
             response_class=PlainTextResponse, dependencies=[Depends(JWTBearer())]),
]
