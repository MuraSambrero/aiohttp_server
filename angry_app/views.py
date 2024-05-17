from aiohttp import web
from schemas import HashRequest
from pydantic import ValidationError
from json.decoder import JSONDecodeError
import services


async def view_hash(request):
    try:
        json_data = await request.json()
        hash_request = HashRequest.model_validate(json_data)
    except ValidationError as e:
        return web.json_response({"validation_errors": str(e)}, status=400)
    except JSONDecodeError as e:
        return web.json_response({"validation_errors": str(e)}, status=400)
    hash_response = await services.service_calc(hash_request)
    return web.json_response(hash_response.model_dump(), status=200)
