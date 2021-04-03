from app.utils.response import JsonResponse
from app.utils.scrape_resource import scrape_resource


async def get_resource_list():
    result = scrape_resource()
    return JsonResponse(data=result)
