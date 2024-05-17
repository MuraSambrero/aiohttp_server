import aiohttp
from app import app
import click


@click.command()
@click.option("--port", default=8000, help="Port to run the web app on")
@click.option("--host", default="0.0.0.0", help="Host to run the web app on")
def run(host, port):
    aiohttp.web.run_app(app, port=port, host=host)




if __name__ == '__main__':
    run()
    