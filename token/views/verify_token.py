from aiohttp import web
from jwt import decode


async def verify_token(request):
    data = await request.json()

    response = decode(data["token"], request.app["config"]["keys"]["public"], algorithms=["ES256"])

    return web.json_response(data=response)
