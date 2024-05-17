from aiohttp import web
import views

routes = web.RouteTableDef()


@routes.get("/healthcheck")
async def healthcheck(request):
    """
    ## healthcheck ендпоинт.
    Тут же возвращает пустой json и статус 200.
    Создаем route
    """
    json_doc = dict()
    return web.json_response(json_doc)


@routes.post("/hash")
async def hash(request):
    """
    ## hash ендпоинт.
    Передает объект request на уровень view и создаем route
    """
    return await views.view_hash(request)
