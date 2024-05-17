from aiohttp import web
import routes
import pytest


@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = web.Application()
    app.router.add_get("/healthcheck", routes.healthcheck)
    app.router.add_post("/hash", routes.hash)
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_healthcheck(cli):
    resp = await cli.get("/healthcheck")
    assert resp.status == 200
    text = await resp.json()
    assert text == dict()


@pytest.mark.asyncio
async def test_hash(cli):
    resp = await cli.post("/hash", json={"string": "test"})
    assert resp.status == 200
    json_data = await resp.json()
    assert (
        json_data["hash_string"]
        == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    )


@pytest.mark.parametrize(
    "json_data_input",
    [
        {"text": "test"},
        dict(),
        None,
        "some_string",
        0,
    ],
)
@pytest.mark.asyncio
async def test_hash_string(cli, json_data_input):
    resp = await cli.post("/hash", json=json_data_input)
    assert resp.status == 400
    json_data = await resp.json()
    assert json_data.get("validation_errors") is not None
