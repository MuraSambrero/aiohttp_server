from aiohttp import web
from routes import routes

def create_app():
    app = web.Application()
    app.add_routes(routes)
    return app

app = create_app()