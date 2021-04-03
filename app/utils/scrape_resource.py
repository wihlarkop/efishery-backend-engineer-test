from functools import lru_cache

import requests

from app.config import settings

@lru_cache()
def scrape_resource():
    CONVERTER_URL = f'{settings.BASE_URL_CONVERTER}/api/v7/convert?q=IDR_USD,USD_IDR&compact=ultra&apiKey={settings.API_KEY_CONVERTER}'

    resource_response = requests.get(settings.RESOURCE_URL).json()
    converter_response = requests.get(CONVERTER_URL).json()

    USD = converter_response.get('IDR_USD')

    result = []

    for item in resource_response:
        if item.get('price') is not None:
            result.append({
                'uuid': item.get('uuid'),
                'komoditas': item.get('komoditas'),
                'area_provinsi': item.get('area_provinsi'),
                'area_kota': item.get('area_kota'),
                'size': item.get('size'),
                'price': {
                    'idr': item.get('price'),
                    'usd': int(item.get('price')) * USD
                },
                'tgl_parsed': item.get('tgl_parsed'),
                'timestamp': item.get('timestamp')
            })

    return result
