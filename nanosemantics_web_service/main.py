from aiohttp import web
from aiohttp_swagger import setup_swagger


from routes import setup_routes
from settings import config
from db import pg_context


def start_server():
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    setup_swagger(app)
    app.cleanup_ctx.append(pg_context)
    web.run_app(app=app)


if __name__ == '__main__':
    start_server()
