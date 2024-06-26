from schemas import HashRequest, HashResponse
from celery_app import hash_calc
import asyncio


async def service_calc(hash_request: HashRequest) -> HashResponse:
    """
    Создание объекта HashResponse и расчет hash для view_hash
    ## Params:
    hash_request: HashRequest - объект pydantic модели с полем string и строкой

    ## Return:
    HashResponse - объект pydantic модели который содержит уже хэшированную строоку
    в поле hash_string
    """
    hash_response: HashResponse = HashResponse(hash_string=hash_request.string)
    hash_response.hash_string = await async_hash_string(
        string_to_hash=hash_request.string
    )
    return hash_response


async def async_hash_string(string_to_hash: str) -> str:
    """
    Передача строки worker'у для расчета hash данной строки
    ## Params:
    string_to_hash: str - строка которую мы передаем изначально в json

    ## Return:
    str - получаем уже хэшированную строку
    """
    result = hash_calc.delay(string_to_hash)
    while not result.ready():
        await asyncio.sleep(0.001)
    return result.result
