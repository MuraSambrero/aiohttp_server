from pydantic import BaseModel

class HashRequest(BaseModel):
    """
    Pydantic модель для предоставления тела запроса пользователя
    ### Params
    - string: str - строка которая будет хеширована
    """
    string: str

class HashResponse(BaseModel):
    """
    Pydantic модель для предоставления тела ответа пользователю
    ### Params
    - hash_string: str - строка которая содержит рассчитанный hash 
    """
    hash_string: str