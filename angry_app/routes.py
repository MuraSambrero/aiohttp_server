from aiohttp import web
import views

routes = web.RouteTableDef()


@routes.get("/healthcheck")
async def healthcheck(request):
    json_doc = dict()
    return web.json_response(json_doc)


@routes.post("/hash")
async def hash(request):
    return await views.view_hash(request)
