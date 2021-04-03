from app.utils.scrape_resource import scrape_resource
from app.utils.response import JsonResponse


async def get_resource_list():
    result = scrape_resource()
    return JsonResponse(data=result)
